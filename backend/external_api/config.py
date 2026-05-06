import os
from dotenv import load_dotenv

load_dotenv()
hardcover_url = os.getenv("hardcover_api_url")
hardcover_token = os.getenv("hardcover_api_key")

if not hardcover_url or not hardcover_token:
    raise RuntimeError("Missing Hardcover API configuration in .env")
