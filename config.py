import os
from dotenv import load_dotenv

load_dotenv()

OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
MODEL_PREFERENCE = os.getenv("MODEL_PREFERENCE", "local")  # "local" or "cloud"
TEMP_DIR = "./temp"
