from aiogram import types

button_menu = [
    [
        types.KeyboardButton(text="База данных"),
        types.KeyboardButton(text="Загрузить")
    ]
]

kb_menu = types.ReplyKeyboardMarkup(
    keyboard=button_menu,
    resize_keyboard=True
)