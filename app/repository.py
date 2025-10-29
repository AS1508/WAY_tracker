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
# (to be added later)