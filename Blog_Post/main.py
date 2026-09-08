from fastapi import FastAPI,Depends,HTTPException
from database import engine,SessionLocal
from sqlalchemy.orm import Session
import models,schemas
from typing import Annotated

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#DB dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# home route
@app.get('/')
def home():
    return {
        "message":"Blog Api started."
    }
    
# blog route
@app.post('/blogs',response_model=schemas.BlogResponse)
def create_blog(blog:schemas.BlogCreate,db:Annotated[Session,Depends(get_db)]):
    new_blog = models.Blog(
        title = blog.title,
        content = blog.content
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

#Read all blog route
@app.get('/blogs',response_model=list[schemas.BlogResponse])
def get_blogs(db:Annotated[Session,Depends(get_db)]):
    return db.query(models.Blog).all()

#Read one blog
@app.get('/blogs/{blog_id}',response_model=schemas.BlogResponse)
def get_blog(blog_id:int,db:Annotated[Session,Depends(get_db)]):
    blog = db.query(models.Blog).filter(models.Blog.id==blog_id).first()
    
    if not blog:
        raise HTTPException(
            status_code=404,
            detail='Blog not found'
        )
    return blog

#update blog API 
@app.put('/blogs/{blog_id}',response_model=schemas.BlogResponse)
def update_blog(blog_id:int,blog:schemas.BlogCreate,db:Annotated[Session,Depends(get_db)]):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not existing_blog:
        raise HTTPException(
            status_code=404,
            detail='Blog not found'
        )
    existing_blog.title = blog.title # type: ignore
    existing_blog.content = blog.content # type: ignore
    
    db.commit()
    
    return existing_blog

#delete blog api
@app.delete('/blogs/{blog_id}')
def delete_blog(blog_id:int,db:Annotated[Session,Depends(get_db)]):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog:
        raise HTTPException(
            status_code=404,
            detail='Blog not found'
        )
    blog.delete()
    db.commit()
    return {
        "message":f'Blog of id:{blog_id} deleted successfully'
    }