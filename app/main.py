# Example main.py
from fastapi import FastAPI
from .routes import router
from app.auth import router as auth_router

app = FastAPI()

app.include_router(router)
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Async FastAPI API up and running"}