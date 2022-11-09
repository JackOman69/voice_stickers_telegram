from aiogram.types import Message
from aiogram import Router
from aiogram.dispatcher.filters import Text
from keyboard import kb_start
from create import ADMINS

router = Router()

@router.message(commands=["start", "help", "Помощь"])
@router.message(Text(text="помощь", text_ignore_case=True))
async def command_start(message: Message):
    if message.from_user.id not in ADMINS:
        await message.answer("❌К сожалению, вы не прошли проверку\n\n❗Позови админа!")
    else:
        await message.answer("✅ Проверка прошла успешно!\n\n🦾 Это админ-бот, предназначенный для добавления голосовых сообщений в базу данных и их обработки\n\n▶ Пришли мне любое голосовое сообщение и следуй инструкциям!", reply_markup=kb_start.kb_menu)