from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     email:str
#     city:str
#     pincode:str
#     occupation:str
#     aadhar:bool
#     pan_card:bool
    
# @app.post('/create-user')
# def create_user(user:User):
#     return {
#         'message':'User Created Successfully.',
#         'data':user
#     }
    
class Address(BaseModel):
    state:str
    city:str
    pincode:str
    
class User(BaseModel):
    name:str
    age:int
    email:str
    address:Address
    
@app.post('/create-user')
def create_user(user:User):
    return {
        'message':'User Created Successfully.',
        'data':user
    }
    