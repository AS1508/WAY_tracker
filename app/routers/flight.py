from fastapi import APIRouter, HTTPException, status
from sqlalchemy import Enum
from ..external import aviationstack_client

router = APIRouter(tags=["Flights(public)"])

class FlightType(str, Enum):
  departure = "departure"
  arrival = "arrival"

@router.get("/flights/{flight_identifier}", response_model=any)
async def get_flight_by_identifier(flight_identifier: str):
  flight_data = await aviationstack_client.fetch_flight_by_icao(flight_identifier)
  if flight_data is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Flight not found"
    )
  return flight_data

@router.get("/flights/airport/{iata_code}", response_model=any)
async def get_flight_by_airport(iata_code: str, flight_type: FlightType = FlightType.departure):
  flight_data = await aviationstack_client.fetch_flight_by_airport(iata_code, flight_type.value)
  if flight_data is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="No flights found for the specified airport and type"
    )
  return flight_data