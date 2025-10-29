from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class UserBase(BaseModel):
  nombre: str = Field(..., max_length=20)
  apellidos: str = Field(..., max_length=30)
  email: str = Field(..., max_length=120)

class UserCreate(UserBase):
  password: str = Field(..., min_length=8, max_length=128)

class UserUpdate(BaseModel):
  nombre: str | None = Field(None, max_length=20)
  apellidos: str | None = Field(None, max_length=30)
  
  model_config = ConfigDict(from_attributes=True)

class User(UserBase):
  id: int
  created_at: datetime
  TrackedFlights: list['TrackedFlight'] = []

  model_config = ConfigDict(from_attributes=True)

class TrackedFlightBase(BaseModel):
  flight_identifier: str = Field(..., max_length=20)

class TrackedFlightCreate(TrackedFlightBase):
  pass

class TrackedFlight(TrackedFlightBase):
  tracked_flight_id: int
  user_id: int
  tracked_at: datetime

  model_config = ConfigDict(from_attributes=True)

class OAuth2PasswordRequestForm(BaseModel):
    username: str
    password: str

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  email: str | None = None

