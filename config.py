import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_PREFERENCE = os.getenv("MODEL_PREFERENCE", "local")  # "local" or "cloud"
TEMP_DIR = "./temp"
