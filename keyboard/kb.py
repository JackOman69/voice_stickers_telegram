from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Беспонтовый")
b2 = KeyboardButton("Деградирующий")
b3 = KeyboardButton("Шизанутый")
b4 = KeyboardButton("Дурка...")


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b1, b2).row(b3, b4)