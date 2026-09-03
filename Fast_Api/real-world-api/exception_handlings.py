from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse

app = FastAPI()

#Custom exception
# 1. Define a custom exception class
class UserNotFoundEception(Exception):
    def __init__(self, name:str):
        self.name = name
        
# 2. Register a global handler for the custom exception
@app.exception_handler(UserNotFoundEception)
def user_not_found_handler(request:Request,exc:UserNotFoundEception):
    return JSONResponse(
        status_code=404,
        content={
            'status':'Simple error',
            'message':f"User {exc.name} not found!"
        }
    )
    
# 3. Use that custom exception handling in url    
@app.get('/user/{name}')
def get_use(name:str):
    if name != 'Anuj':
        raise UserNotFoundEception(name)
    return {
        'name':name
    }

# @app.get('/users/{user_id}')
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail='User not found!'
#         )
#     return {
#         'id':1,
#         'name':'Mohan Yadav'
#     } 