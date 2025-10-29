import httpx
from .. import config

BASE_PARAMS = {"access_key": config.AVIATIONSTACK_API_KEY}
BASE_URL = config.AVIATIONSTACK_BASE_URL

async def fetch_flight_by_icao(flight_icao: str) -> dict | None:
  params = BASE_PARAMS.copy()
  params["flight_icao"] = flight_icao

  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(f"{BASE_URL}/flights", params=params)
      response.raise_for_status()

      data = response.json()
      if data and data.get("data"):
        return data["data"][0]
      return None
    except httpx.HTTPStatusError as e:
      print(f"Error fetching flight data: {e}")
      return None
    except httpx.RequestError as e:
      print(f"Request error: {e}")
      return None

async def fetch_flight_by_airport(iata_code: str, flight_type: str = "departure") -> dict | None:
  params = BASE_PARAMS.copy()

  if flight_type == "departure":
    params["dep_iata"] = iata_code
  elif flight_type == "arrival":
    params["arr_iata"] = iata_code
  else:
    raise ValueError("flight_type must be either 'departure' or 'arrival'")

  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(f"{BASE_URL}/flights", params=params)
      response.raise_for_status()

      data = response.json()
      if data and data.get("data"):
        return data["data"]
      return None
    except httpx.HTTPStatusError as e:
      print(f"Error fetching flight data: {e}")
      return None
    except httpx.RequestError as e:
      print(f"Request error: {e}")
      return None
