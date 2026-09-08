import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    Database_url = os.getenv("DATABASE_URL")
    
settings = Settings