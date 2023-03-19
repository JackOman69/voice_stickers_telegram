from fastapi import FastAPI
from pydantic import BaseModel
from database.postgres import check_deleted_voice, id_created_voice, get_all, voice_by_id, voice_by_name, voice_by_tag, tags_sorted_by_authors, voice_by_author, all_voices_by_author, create_the_voice, delete_the_voice, edit_the_voice

app = FastAPI(
    title="VoiceStickersAPI",
    description="VoiceStickers Telegram API for creating and manage your own voices 🚀",
    contact={
        "name": "JackOMan69",
        "url": "https://github.com/JackOMan69"
    }
)


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


BASE_URL = "/bot/"


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


# Получение голосовых по именам, тегам, авторам
@app.get(BASE_URL + "get_voices/")
async def get_voices(text: str):
    result = []

    text = text.lower().strip()

    voices = get_all()
    for voice in voices:
        isFind = False

        name = voice[2].lower()
        if name.find(text) != -1:
            isFind = True

        if isFind == False:
            author = voice[5].lower()
            if author.find(text) != -1:
                isFind = True

        if isFind == False:
            tags = voice[4]
            if (name in tags):
                isFind = True

        if isFind:
            result.append({
                "id": voice[0],
                "voice": voice[1],
                "name": voice[2],
                "description": voice[3],
                "tags": voice[4],
                "author": voice[5],
                "created_date": voice[6],
                "admin_author_id": voice[7]
            })
    
    if len(result) == 0 and len(text) == 0:
        for voice in voices:
            result.append({
                "id": voice[0],
                "voice": voice[1],
                "name": voice[2],
                "description": voice[3],
                "tags": voice[4],
                "author": voice[5],
                "created_date": voice[6],
                "admin_author_id": voice[7]
            })

    return result


@app.get(BASE_URL + "tags/")
async def get_voice_by_tag(tag: str):
    sorted_by_tag = []
    for i in voice_by_tag(tag):
        single_by_tag = {
            "id": i[0],
            "voice": i[1],
            "name": i[2],
            "description": i[3],
            "tags": i[4],
            "author": i[5],
            "created_date": i[6],
            "admin_author_id": i[7]
        }
        sorted_by_tag.append(single_by_tag)
    return sorted_by_tag


@app.get(BASE_URL + "tags/sorted")
async def sorted_tags_by_author(author: str):
    tags_by_authors = []
    for i in tags_sorted_by_authors(author):
        single_tag = {
            "tags": i[0]
        }
        tags_by_authors.append(single_tag)
    return tags_by_authors


@app.get(BASE_URL + "authors/")
async def get_voice_by_author(author: str):
    sorted_by_author = []
    for i in voice_by_author(author):
        single_by_author = {
            "id": i[0],
            "voice": i[1],
            "name": i[2],
            "description": i[3],
            "tags": i[4],
            "author": i[5],
            "created_date": i[6],
            "admin_author_id": i[7]
        }
        sorted_by_author.append(single_by_author)
    return sorted_by_author


@app.get(BASE_URL + "authors/all")
async def get_voice_by_author():
    all_authors = []
    for i in all_voices_by_author():
        single_author = {
            "author": i[0]
        }
        all_authors.append(single_author)
    return all_authors


@app.post(BASE_URL + "create/")
async def create_new_voice(bot: Create):
    create_the_voice(bot.voice, bot.name, bot.description,
                     bot.tags, bot.author, bot.admin_author_id)
    create_result = {
        "result": "OK",
        "id": id_created_voice()
    }
    return create_result


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
