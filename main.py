from aiogram import executor
from create import dp
from handlers import add_voices, start_chat, sort_by_tags
from database import sql_db

async def on_startup(_):
    sql_db.sql_start()

start_chat.answer_handler(dp)

sort_by_tags.database_handler(dp)

add_voices.add_shiz(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)