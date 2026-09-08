from pydantic import BaseModel

class BlogCreate(BaseModel):
    content:str
    title:str
    
class BlogResponse(BaseModel):
    id:int
    title:str
    content:str
 
class Config:
    from_attributes = True   