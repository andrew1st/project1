from fastapi import FastAPI

app = FastAPI()

@app.get("/")

@app.get("/protected")

async def root():
    return {"message": "Welcome to the Asynchronous FastAPI project!"}
