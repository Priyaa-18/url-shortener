from fastapi import FastAPI, HTTPException
from app.database import SessionLocal, Base, engine
from app import models

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to URL Shortener!"}
