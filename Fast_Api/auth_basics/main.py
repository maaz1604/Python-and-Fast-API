from fastapi import FastAPI,HTTPException,Header,Depends
from jose import jwt
from datetime import datetime,timedelta,timezone
from typing import Annotated

app = FastAPI()

SECRET_KEY = 'josua58746'

ALGORITHM = "HS256"

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update(
        {
            "exp":expire
        }
    )
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
    return token

#generate token by Login API
@app.post('/login')
def login(username:str,password:str):
    if username != 'admin' or password != '1234':
        raise HTTPException(
            status_code=401,
            detail='Invalid username and password! Please try again.'
        )
    token = create_token({
        "sub":username
    })
    return {
        'access_token':token
    }
    
#Token verification
def verify_token(token:str = Header(None)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail='Invalid or expired token!'
        )
        
#Protected route
@app.get('/secure')
def secure_data(user:Annotated[dict,Depends(verify_token)]):
    return {
        'message':'Secure data access.',
        'data':user
    }