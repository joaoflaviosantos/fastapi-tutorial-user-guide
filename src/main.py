"First Documetation Exemple"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    'Retuns {"message": "Hello World"} message.'
    return {"message": "Hello World"}
