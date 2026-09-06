from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings

app = FastAPI()

# Origins must match the browser Origin header exactly (without a trailing slash).
origin=settings.origins
Secret_key = settings.secret

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin] if origin else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return {'message':"Cors enabled"}