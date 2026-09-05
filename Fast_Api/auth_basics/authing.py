import bcrypt
from fastapi import FastAPI,HTTPException,Depends
from jose import jwt
from jose.exceptions import JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime,timedelta,timezone
from typing import Annotated

app = FastAPI()

SECRET_KEY = 'josua58746'

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MIN=30

# Passwords are encoded explicitly so this works with bcrypt 5.x without
# relying on passlib's incompatible backend detection.
def _password_bytes(password: str) -> bytes:
    password_bytes = password.encode("utf-8")
    if len(password_bytes) > 72:
        raise ValueError("Password must be 72 bytes or fewer.")
    return password_bytes

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

# Dummy user db
fake_user_db = {
    'admin':{
        'username':'admin',
        'hashed_password':bcrypt.hashpw(_password_bytes('1234'), bcrypt.gensalt()).decode()
    }
}

#hashed password
def hashed_password(password:str):
    return bcrypt.hashpw(_password_bytes(password), bcrypt.gensalt()).decode()

#verify password
def verify_password(plain_password: str, hashed_password: str):
    try:
        return bcrypt.checkpw(
            _password_bytes(plain_password),
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        return False

# Create token
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

#generate token by OAuth2 form
@app.post('/login')
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user['hashed_password']):
        raise HTTPException(
            status_code=400,
            detail='Invalid username and password! Please try again.'
        )
    access_token = create_token({"sub":form_data.username})
    return {
        'access_token':access_token,
        "token_type":"bearer"
    }
    
#Token verification
def verify_token(token:Annotated[str,Depends(oauth2_schema)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        
        username=payload.get("sub") 
        if username is None:
            raise HTTPException(
                status_code=401,
                detail='Invalid token!'
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail='INvalid token!'
        )
        
#Protected route
@app.get('/secure')
def protected_route(username:Annotated[dict,Depends(verify_token)]):
    return {
        'message':f'Hello {username}, you have access to this protected route.',
        "user":username
    }