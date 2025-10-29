from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  nombre = Column(String(20), nullable=False, index=True)
  apellidos = Column(String(30), nullable=False)
  email = Column(String(120), unique=True, nullable=False, index=True)
  encrypted_password = Column(String(255), nullable=False)
  created_at = Column(DateTime, server_default=func.now())

  tracked_flights = relationship('TrackedFlight', back_populates='owner')

class TrackedFlight(Base):
  __tablename__ = 'tracked_flights'

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
  flight_identifier = Column(String(20), nullable=False, index=True)
  tracked_at = Column(DateTime, server_default=func.now())

  owner = relationship('User', back_populates='tracked_flights')