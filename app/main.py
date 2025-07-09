## This page we are going to implement the main application logic, including the FastAPI app and the routes.

from fastapi import FastAPI, Depends, HTTPException
from app.database import SessionLocal, engine, base
from app.models import JournalEntry
from app.routes import router

# Create a FastAPI application instance
app = FastAPI()

# Create the database tables
base.metadata.create_all(bind=engine)

#root end point
@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather Journal API!"}

# Add the API routes
app.include_router(router)
