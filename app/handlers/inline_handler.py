from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultCachedVoice
import httpx
import uuid

router = Router()

@router.inline_query()
async def inline_handler_search(inline: InlineQuery):
    text = inline.query
    inline_list_voices = []
    async with httpx.AsyncClient() as client:
        response = await client.get("http://api/bot/names/?name=" + text.capitalize())
        voices_parsed = response.json()
    if not text:
        for i in range(45):
            result_id = str(uuid.uuid4())
            inline_list_voices.append(InlineQueryResultCachedVoice(
                type = "voice",
                id = result_id,
                voice_file_id = voices_parsed[i]["voice"],
                title = voices_parsed[i]["name"]
            ))
    else:
        inline_list_voices = []
        for i in voices_parsed:
            result_id = str(uuid.uuid4())
            inline_list_voices.append(InlineQueryResultCachedVoice(
                type = "voice",
                id = result_id,
                voice_file_id = i["voice"],
                title = i["name"]
            ))
    await inline.answer(inline_list_voices, cache_time = 1, is_personal=True)
    