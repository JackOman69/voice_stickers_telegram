from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultCachedVoice

import httpx
import uuid
import os

router = Router()


@router.inline_query()
async def inline_handler_search(inline: InlineQuery):
    text = inline.query

    async with httpx.AsyncClient() as client:
        response = await client.get(os.getenv("HOST") + "/bot/get_voices/?text=" + text)
        voices = response.json()

    voices = list(reversed(voices))
    if len(voices) > 45:
        range_num = 45
    else:
        range_num = len(voices)

    result_voices = []
    for i in range(range_num):
        result_voices.append(InlineQueryResultCachedVoice(
            type="voice",
            id=str(uuid.uuid4()),
            voice_file_id=voices[i]["voice"],
            title=voices[i]["name"]
        ))

    await inline.answer(result_voices, cache_time=1, is_personal=True)
