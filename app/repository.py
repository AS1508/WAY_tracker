from sqlalchemy.orm import Session
from . import models

# --- User Functions ---

def create_user(db: Session, user: models.User) -> models.User:
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def get_user_by_email(db: Session, email: str) -> models.User | None:
  return db.query(models.User).filter(models.User.email == email).first()

def update_user_db(db: Session, user: models.User) -> models.User:
  db.commit()
  db.refresh(user)
  return user

def delete_user_db(db: Session, user: models.User):
  db.delete(user)
  db.commit()


# --- Flight Functions ---
def get_flight_by_user_and_identifier(
  db: Session,
  user_id: int,
  flight_identifier: str
) -> models.Flight | None:
  return db.query(models.Flight).filter(
    models.Flight.user_id == user_id,
    models.Flight.flight_identifier == flight_identifier
  ).first()

def save_tracked_flight(
  db: Session,
  flight_model: models.TrackedFlight
) -> models.TrackedFlight:
  db.add(flight_model)
  db.commit()
  db.refresh(flight_model)
  return flight_model