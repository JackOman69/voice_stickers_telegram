from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_menu = KeyboardButton("Меню")
button_load = KeyboardButton("Загрузить")

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.row(button_menu, button_load)