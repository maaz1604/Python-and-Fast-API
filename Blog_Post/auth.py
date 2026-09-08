from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from config import settings

access_exp = settings.access_token_exp


oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=float(access_exp or 30))
    to_encode.update({"exp":expire})
    if settings.secret_key is None:
        raise ValueError("SECRET_KEY must be configured")
    if settings.algorithm is None:
        raise ValueError("Please configure your algorithm")
    return jwt.encode(to_encode,settings.secret_key,algorithm=settings.algorithm)

def verify_token(token:Annotated[str,Depends(oauth2_schema)]):
    try:
        if settings.secret_key is None:
            raise ValueError("SECRET_KEY must be configured")
        if settings.algorithm is None:
            raise ValueError("Please configure your algorithm")
        payload = jwt.decode(token,settings.secret_key,algorithms=settings.algorithm)
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail='Invalid token'
        )