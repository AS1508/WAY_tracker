import os
from dotenv import load_dotenv

load_dotenv()

# --- Database configuration --- #
DATABASE_URL = os.getenv("URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables.")

# --- Security and JWT configuration --- #
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in environment variables.")

ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# --- External API configuration --- #
AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
if not AVIATIONSTACK_API_KEY:
    raise ValueError("AVIATIONSTACK_API_KEY is not set in environment variables.")
AVIATIONSTACK_BASE_URL = "http://api.aviationstack.com/v1"