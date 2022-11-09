from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultCachedVoice

from database import sql_db

router = Router()

@router.inline_query()
async def inline_handler_search(inline: InlineQuery):
    text = inline.query
    voices = []
    raw_voices = await sql_db.sql_sort_by_name(text)
    voices_parsed = [list(i) for i in raw_voices]
    result_id = 0
    for i in voices_parsed:
        result_id += 1
        voices.append(InlineQueryResultCachedVoice(
            type = "voice",
            id = result_id,
            voice_file_id = i[1],
            title = i[2]
        ))
    await inline.answer(voices, cache_time=1, is_personal=True)