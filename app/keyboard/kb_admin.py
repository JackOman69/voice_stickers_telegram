from aiogram import types

button_cancel = [
    [
        types.KeyboardButton(text="Отмена")
    ]
]

kb_cancel = types.ReplyKeyboardMarkup(
    keyboard=button_cancel, 
    resize_keyboard=True
)
