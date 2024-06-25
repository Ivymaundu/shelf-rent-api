from fastapi import FastAPI
from dbservice import *
from schemas import *
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
db = SessionLocal()

origins = [
    "http://localhost",
    "http://localhost:5173"
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
