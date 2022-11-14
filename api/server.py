from fastapi import FastAPI
from pydantic import BaseModel
from database.postgres import voice_by_id, voice_by_name, voice_by_tag, voice_by_author

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

@app.get(BASE_URL + "?id={id}")
async def get_voice_by_id(id: str):
    sorted_by_id = {}
    for i in voice_by_id(id):
        sorted_by_id = {
            "id": i[0],
            "voice": i[1],
            "name": i[2],
            "description": i[3],
            "tags": i[4],
            "author": i[5],
            "created_date": i[6],
            "admin_author_id": i[7]
        }
    return sorted_by_id

@app.get(BASE_URL + "?name={name}")
async def get_voice_by_name(name: str):
    sorted_by_name = {}
    for i in voice_by_name(name):
        sorted_by_name = {
            "id": i[0],
            "voice": i[1],
            "name": i[2],
            "description": i[3],
            "tags": i[4],
            "author": i[5],
            "created_date": i[6],
            "admin_author_id": i[7]
        }
    return sorted_by_name

@app.get(BASE_URL + "?tag={tag}")
async def get_voice_by_tag(tag: str):
    sorted_by_tag = {}
    for i in voice_by_tag(tag):
        sorted_by_tag = {
            "id": i[0],
            "voice": i[1],
            "name": i[2],
            "description": i[3],
            "tags": i[4],
            "author": i[5],
            "created_date": i[6],
            "admin_author_id": i[7]
        }
    return sorted_by_tag

@app.get(BASE_URL + "?author={author}")
async def get_voice_by_author(author: str):
    sorted_by_author = {}
    for i in voice_by_author(author):
        sorted_by_author = {
            "id": i[0],
            "voice": i[1],
            "name": i[2],
            "description": i[3],
            "tags": i[4],
            "author": i[5],
            "created_date": i[6],
            "admin_author_id": i[7]
        }
    return sorted_by_author


