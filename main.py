from aiogram import executor
from create import dp
from handlers import client, admin
from database import sql_db

async def on_startup(_):
    sql_db.sql_start()

client.answer_handler(dp)

admin.add_shiz(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)