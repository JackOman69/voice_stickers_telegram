from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboard import kb_start

ADMIN_ID = [509237723, 458554554, 440280067]

async def command_start(message: types.Message):
    global ADMIN_ID
    if message.from_user.id not in ADMIN_ID:
        await message.answer("К сожалению, вы не прошли проверку, позови админа!")
    else:
        await message.answer("Ну привет!\nЭто админ-бот, предназначенный для добавление голосовых в базу данных и её просмотра\nПришли мне любое голосовое сообщение и следуй инструкциям!", reply_markup=kb_start.kb_menu)

def answer_handler(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "Помощь"])
    dp.register_message_handler(command_start, Text(equals="помощь", ignore_case=True))