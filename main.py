import logging
from aiogram import executor
from create import dp
from handlers import add_voices, start_chat, sort_by_tags
from database.sql_db import sql_start

async def on_startup(_):
    sql_start()
    
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

start_chat.answer_handler(dp)
sort_by_tags.database_handler(dp)
add_voices.register_voices(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)