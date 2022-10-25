from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_cancel = KeyboardButton("Отмена")

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)
