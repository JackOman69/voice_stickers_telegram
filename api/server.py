from fastapi import FastAPI
from pydantic import BaseModel
from database.postgres import check_deleted_voice, id_created_voice, get_all, voice_by_id, voice_by_name, voice_by_tag, voice_by_author, create_the_voice, delete_the_voice, edit_the_voice

app = FastAPI()

class Create(BaseModel):
    voice: str
    name: str
    description: str
    tags: list
    author: str
    admin_author_id: int

class Edit(BaseModel):
    name: str
    description: str
    tags: list
    author: str

BASE_URL = "/api/bot/"

@app.get(BASE_URL + "all")
async def get_all_bd():
    all_voices = []
    for i in get_all():
        single_voice = {
            "id": i[0],
            "voice": i[1],
            "name": i[2],
            "description": i[3],
            "tags": i[4],
            "author": i[5],
            "created_date": i[6],
            "admin_author_id": i[7]
        }
        all_voices.append(single_voice)
    return all_voices

@app.get(BASE_URL + "id/")
async def get_voice_by_id(id: int):
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

@app.get(BASE_URL + "name/")
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

@app.get(BASE_URL + "tag/")
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

@app.get(BASE_URL + "author/")
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

@app.post(BASE_URL + "create/")
async def create_new_voice(bot: Create):
    create_the_voice(bot.voice, bot.name, bot.description, bot.tags, bot.author, bot.admin_author_id)
    result = {
        "result": "OK",
        "id": id_created_voice()
    }
    return result

@app.delete(BASE_URL + "delete/")
async def delete_existing_voice(id: int):
    if check_deleted_voice(id):
        return {"status": "DELETED"}
    else:
        delete_the_voice(id)
        return {"status": "OK"}

@app.put(BASE_URL + "edit/")
async def edit_existing_voice(bot: Edit, id: int):
    edit_the_voice(bot.name, bot.description, bot.tags, bot.author, id)
    get_voice_by_id(id)