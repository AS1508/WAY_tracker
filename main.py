from fastapi import FastAPI
from routers import auth, user, flight
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
  title="WAY Tracker API",
  description="Plataforma de seguimiento de vuelos de WAY.",
  version="0.1.0"
)

@app.get("/")
async def read_root():
  return {"message": "Bienvenido a WAY Tracker API"}

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(flight.router)
