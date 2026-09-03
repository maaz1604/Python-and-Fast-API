from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    city:str
    pincode:str
    role:str
    
# Post request
@app.post('/create-user')
def create_user(user:User):
    return {
        'message':'User Created Successfully',
        'data':user
    }