from pydantic import BaseModel, Field
from sqlalchemy import DateTime

class UserBase(BaseModel):
  nombre: str = Field(..., max_length=20)
  apellidos: str = Field(..., max_length=30)
  email: str = Field(..., max_length=120)

class UserCreate(UserBase):
  password: str = Field(..., min_length=8, max_length=128)

class User(UserBase):
  id: int
  created_at: DateTime
  TrackedFlights: list['TrackedFlight'] = []

  class Config:
    orm_mode = True

class TrackedFlightBase(BaseModel):
  flight_number: str = Field(..., max_length=20)

class TrackedFlightCreate(TrackedFlightBase):
  pass

class TrackedFlight(TrackedFlightBase):
  id: int
  user_id: int
  timestamp: DateTime

  class Config:
    orm_mode = True

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  email: str | None = None

