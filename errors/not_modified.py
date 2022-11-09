from aiogram import types, Router
from aiogram.exceptions import TelegramBadRequest

router = Router()

@router.errors()
async def message_not_modified(update: types.Update, exception: TelegramBadRequest):
    return True