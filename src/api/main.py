from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/hello")
async def hello(id: int = 0):
    print(id)
    return {"message": "hello world!!!!!"}
