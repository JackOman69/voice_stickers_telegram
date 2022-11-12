from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Bot(BaseModel):
    id: int
    voice: str
    name: str
    description: str
    tags: str
    author: str
    created_date: str
    admin_author_id: int

BASE_URL = "/api/bot/"

@app.get(BASE_URL)
async def root():
    return {"message": "Hello world!"}

