from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import models, schemas, security, repository

# --- User Services --- #
def register_new_user(db: Session, user: schemas.UserCreate) -> models.User:
  db_user = repository.get_user_by_email(db, email=user.email)
  if db_user:
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="The email is already registered"
    )

  hashed_password = security.get_password_hash(user.password)

  db_user_model = models.User(
    email=user.email,
    nombre=user.nombre,
    apellido=user.apellido, 
    hashed_password=hashed_password
  )

  return repository.create_user(db=db, user=db_user_model)

def authenticate_user(db: Session, email: str, password: str) -> models.User | None:
  user = repository.get_user_by_email(db, email=email)

  if not user:
    return None

  if not security.verify_password(password, user.hashed_password):
    return None

  return user

def login_user(db: Session, form_data: schemas.OAuth2PasswordRequestForm) -> schemas.Token:
  user = authenticate_user(
    db=db, 
    email=form_data.username, 
    password=form_data.password
  )

  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid email or password",
      headers={"WWW-Authenticate": "Bearer"},
    )

  expires = timedelta(minutes=int(security.ACCESS_TOKEN_EXPIRE_MINUTES))

  access_token = security.create_access_token(
    data={"sub": user.email}, 
    expires_delta=expires
  )
  return {"access_token": access_token, "token_type": "bearer"}

def update_user_profile(
  db: Session,
  user_model: models.User,
  user_update_data: schemas.UserUpdate
) -> models.User:

  update_data = user_update_data.model_dump(exclude_unset=True)
  
  for key, values in update_data.items():
    setattr(user_model, key, values)
  
  return repository.update_user_db(db=db, user=user_model)

def delete_user_account(db: Session, user_model: models.User):
  repository.delete_user_db(db=db, user=user_model)

# --- Flight Services --- #
def track_flight_for_user(
  db: Session,
  user_model: models.User,
  flight_data: schemas.FlightTrackRequest
) -> models.TrackedFlight:

  existing_flight = repository.get_flight_by_user_and_identifier(
    db=db,
    user_id=user_model.id,
    flight_identifier=flight_data.flight_identifier
  )

  if existing_flight:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="The flight is already being tracked for this user"
    )

  flight_model = models.TrackedFlight(
    user_id=user_model.id,
    flight_identifier=flight_data.flight_identifier,
  )

  return repository.save_tracked_flight(db=db, flight_model=flight_model)