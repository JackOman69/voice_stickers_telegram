from aiogram import types, Dispatcher

async def command_start(message: types.Message):
    await message.answer("Ну привет!\nЭтот бот предназначен для создания голосовых сообщений с их описанием и быстрым использованием")

def answer_handler(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])