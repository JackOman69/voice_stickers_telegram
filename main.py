from aiogram import executor
from create import dp
from handlers import client, admin

client.answer_handler(dp)

admin.add_shiz(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)