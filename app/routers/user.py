from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from .. import schemas, models, security, database, services

router = APIRouter(
  prefix="/me",
  tags=["Users (Me)"]
)

@router.get("/", response_model=schemas.User)
def read_users_me(current_user: models.User = Depends(security.get_current_user)):
  return current_user

@router.patch("/profile", response_model=schemas.User)
def update_user_profile(
  user_update: schemas.UserUpdate,
  current_user: models.User = Depends(security.get_current_user),
  db: Session = Depends(database.get_db)
):
  return services.update_user_profile(db, current_user, user_update)

@router.delete("/account", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_account(
  current_user: models.User = Depends(security.get_current_user),
  db: Session = Depends(database.get_db)
):
  services.delete_user_account(db, current_user)
  return Response(status_code=status.HTTP_204_NO_CONTENT)