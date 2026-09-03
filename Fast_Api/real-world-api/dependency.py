from fastapi import FastAPI,Depends, Header, HTTPException
from typing import Annotated

app = FastAPI()

def common_logic():
    return {
        'message':'Common Logic Executed'
    }
    
#Old way
# @app.get('/home')
# def home(data=Depends(common_logic)):
#     return data 

# New way by using Annotated 
@app.get('/home')
def home(data:Annotated[dict,Depends(common_logic)]):
    return data

def get_current_user():
    return {
        'user':'Raghav Chadda',
        'email':'raghav@gmail.com',
        'location':'delhi'
    }
    
@app.get('/profile')
def profile(user:Annotated[dict,Depends(get_current_user)]):
    return user

@app.get('/dashboard')
def dash(user:Annotated[dict,Depends(get_current_user)]):
    return user

# using header
def verify_token(token:str=Header(None)):
    if token != 'mysecrettoken':
        raise HTTPException(
            status_code=401,
            detail='Unauthorized access!'
        )
    return {
        'user':{
            'status':'Authorized user',
            'name':'Raghu Trivedi',
            'email':'raghu@gmail.com',
            'phone':457896213,
            'address':'Bathoi,Uttar Pradesh,India'
        }
    }
    
@app.get('/secure-data')
def secure_data(user:Annotated[dict,Depends(verify_token)]):
    return {
        'message':'Secured data accessed.',
        'user':user
    }