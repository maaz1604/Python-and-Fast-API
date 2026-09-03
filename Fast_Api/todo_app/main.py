from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool
    
@app.post('/todos')
def create_todos(todo:Todo):
    todos.append(todo)
    return{
        'message':'Todo created successfully.',
        'data':todo
    }
    
@app.get('/todos')
def get_todos():
    return todos

@app.get('/todos/{todo_id}')
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {'error':'Todo is not found!'}

@app.put('/todos/{todo_id}')
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                'message': f'Todo of which id:{todo_id} is successfuly updated',
                'data':updated_todo
            }
    return {'error':'Todo is not found!'}

@app.delete('/todos/{todo_id}')
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return{
                "message":f'Todo of which id:{todo_id} is sucessfully deleted.'
            }
    return {'error':'Todo is not found!'}

