from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker, declarative_base,Session
from fastapi import FastAPI,Depends,HTTPException
from typing import Annotated


app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    completed = Column(String)
    
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Ceate Api
@app.post('/todos')
def create_todo(title:str,db:Annotated[Session,Depends(get_db)]):
    todo = Todo(title=title,completed='False')
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        'message':'Todo is successfully created.',
        'data':todo
    }
    
#Read all data
@app.get('/todos')
def get_todos(db:Annotated[Session,Depends(get_db)]):
    todos = db.query(Todo).all()
    return {
        'Total':len(todos),
        'data':todos
    }
    
#fetching data according to id
@app.get('/todos/{todo_id}')
def get_todo(todo_id:int,db:Annotated[Session,Depends(get_db)]):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if not todo:
        raise HTTPException(
            status_code=404,
            detail='Todo not found!'
        )
    return todo

#Update
@app.put('/todos/{todo_id}')
def update_todo(todo_id:int,title:str,db:Annotated[Session,Depends(get_db)],completed:bool):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
        raise HTTPException(
            status_code=404,
            detail='Todo not found!'
        )
        
    todo.title = title
    todo.completed = completed
    
    db.commit()
    db.refresh(todo)
    
    return {
    'message':f'Todo:{todo_id} updated successfully.',
    'data':todo        
    }
    
@app.delete('/todos/{todo_id}')
def update_todo(todo_id:int,db:Annotated[Session,Depends(get_db)]):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
        raise HTTPException(
            status_code=404,
            detail='Todo not found!'
        )
    
    db.delete(todo)
    db.commit()
    # db.refresh(todo)
    
    return{
        'message':f'Todo of id={todo_id} is deleted successfully.',
        'data':todo
    }