import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    origins = os.getenv("origins")
    secret = os.getenv("secret")
    
settings = Settings