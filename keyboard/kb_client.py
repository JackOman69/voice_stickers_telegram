from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_cancel = KeyboardButton("Отмена")

b1 = KeyboardButton("Беспонтовый")
b2 = KeyboardButton("Деградирующий")
b3 = KeyboardButton("Шизанутый")
b4 = KeyboardButton("Дурка...")

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)

kb_choose = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_choose.row(b1, b2).row(b3, b4).add(button_cancel)