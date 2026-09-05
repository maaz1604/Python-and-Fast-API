from fastapi import FastAPI,HTTPException,File,UploadFile
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# 1 - Ensure folder exists
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
    
# 2 - Static file setup
app.mount('/files',StaticFiles(directory=UPLOAD_DIR),name="files")

# 3 - upload file api
@app.post('/upload')
def upload_file(file:UploadFile = File(...)):
    filename = file.filename
    if not filename:
        raise HTTPException(
            status_code=400, 
            detail="Filename is missing"
            )
    file_path = os.path.join(UPLOAD_DIR,filename)
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        
        return {
            'message':'File uploaded successfully',
            'filename':filename,
            'file_url':f'http://127.0.0.1:8000/files/{filename}'
        }
        
# 4 - Get file url api
@app.get('/files/{filename}')
def get_file(filename:str):
    file_path = os.path.join(UPLOAD_DIR,filename)
    if not filename:
        raise HTTPException(
            status_code=400, 
            detail="Filename is missing"
            )
    return {
        'File_URL':f'http://127.0.0.1:8000/files/{filename}'
    }
    
@app.get('/')
def home():
    return{
        'message':'File upload is running.'
    }