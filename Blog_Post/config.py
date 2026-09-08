import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    Database_url = os.getenv("DATABASE_URL")
    secret_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM")
    access_token_exp = os.getenv("ACCESS_TOKEN_EXPIRE_MIN")
    
settings = Settings