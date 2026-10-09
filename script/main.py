import logging
import os
import sys
from dotenv import load_dotenv

#load_dotenv()

# --- Logger Configuration ---
logging.basicConfig(
    level="INFO",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
LOGGER = logging.getLogger(__name__)


ENVIRONMENT = os.getenv('env')
load_dotenv(f"{os.path.dirname(__file__)}/.env.{ENVIRONMENT}")
print(f"Loaded environment variables from .env.{ENVIRONMENT}")


ENV = os.getenv('API')
print(f"ENV: {ENV}")