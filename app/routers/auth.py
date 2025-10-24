from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from .. import database, models, schemas, security, services

router = APIRouter(
  prefix="/auth",
  tags=["auth"],
)
# --- User Endpoints --- #
@router.post("/register", response_model=schemas.User)
def register_user(
  user: schemas.UserCreate, 
  db: Session = Depends(database.get_db)
):
  return services.register_new_user(db=db, user=user)

@router.post("/login", response_model=schemas.Token)
def login_for_access_token(
  db: Session = Depends(database.get_db),
  form_data: OAuth2PasswordRequestForm = Depends()
):
  return services.login_user(db=db, form_data=form_data)

# --- Flight Endpoints --- #
# (to be added later)