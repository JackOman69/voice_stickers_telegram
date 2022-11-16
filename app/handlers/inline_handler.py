from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultCachedVoice
import httpx

router = Router()

@router.inline_query()
async def inline_handler_search(inline: InlineQuery):
    text = inline.query
    inline_list_voices = []
    async with httpx.AsyncClient() as client:
        response = await client.get("http://api/bot/names/?name=" + text.capitalize())
        voices_parsed = response.json()
    result_id = 0
    for i in voices_parsed:
        result_id += 1
        inline_list_voices.append(InlineQueryResultCachedVoice(
            type = "voice",
            id = result_id,
            voice_file_id = i["voice"],
            title = i["name"]
        ))
    await inline.answer(inline_list_voices, cache_time=1, is_personal=True)
    