from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get('/')
def home():
    return{
        'message':'Welcome to the Home Page!'
    }
    
# About Route
@app.get('/about')
def about():
    return {
        'message':'This is About Page.'
    }
    
# User page - Path parameters
@app.get('/users/{user_id}')
def users(user_id:int):
    return {
        'user_id':user_id
    }
    
#Product page - Query parameters
@app.get('/products')
def products(name:str=None):
    return{
        'name':name
    }
    
# Handling multiple query parameters
@app.get('/items')
def item_info(name:str=None,price:int=10):
    return{
        'name':name,
        'price':price 
    }
    
# Post request
@app.post('/create-user')
def create_user(user:dict):
    return {
        'message':'User Created Successfully',
        'data':user
    }