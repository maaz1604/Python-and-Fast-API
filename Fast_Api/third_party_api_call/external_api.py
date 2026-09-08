# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# data = response.json()

# print(data)

from fastapi import FastAPI,HTTPException
import requests

app = FastAPI()

@app.get('/posts')
def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url=url)
    if response.status_code != 200:
            raise HTTPException(
                status_code=404,
                detail='Page not found!'
            )
    data = response.json()
    return data[:10]

#get single post
@app.get('/posts/{post_id}')
def get_post_by_id(post_id:int):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.get(url=url)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail='Page not found!'
        )
    data = response.json()
    return {'message':f'Data of id:{post_id} fetched successfully','data':data}