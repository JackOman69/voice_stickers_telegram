from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from database import sql_db
from keyboard import kb_start

async def command_start(message: types.Message):
    await message.answer("Ну привет!\nЭтот бот предназначен для создания голосовых сообщений с их описанием и быстрым использованием", reply_markup=kb_start.kb_menu)

async def shiz_menu(message: types.Message):
    await sql_db.sql_read(message)

def answer_handler(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(shiz_menu, commands=["Меню"])
    dp.register_message_handler(shiz_menu, Text(equals="меню", ignore_case=True))