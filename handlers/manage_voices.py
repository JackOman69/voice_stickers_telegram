from email.message import Message
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified, MessageToDeleteNotFound
from create import dp, bot
from handlers import sort_by_tags
from database import sql_db

def get_keyboard(i):
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(text="Посмотреть", callback_data=f"description_show {i[0]}"),
        types.InlineKeyboardButton(text="Скрыть", callback_data=f"description_hide {i[0]}")
    ).add(types.InlineKeyboardButton(text="Удалить", callback_data=f"description_delete {i[0]}")
    ).add(types.InlineKeyboardButton(text="Назад", callback_data=f"description_back"))

@dp.callback_query_handler(Text(startswith="description_show"))
async def show_description(callback: types.CallbackQuery):
    edit = await sql_db.sql_edit(callback.data.replace("description_show ", ""))
    for i in edit:
        await bot.edit_message_text(
            f"ID в базе данных: {i[0]}\nНазвание голосового: {i[2]}\nОписание голосового: {i[3]}\nТеги голосового: {i[4]}\nАвтор голосового: {i[5]}\nID Автора: {i[7]}", 
            callback.from_user.id, 
            callback.message.message_id, 
            reply_markup=get_keyboard(i)
        ) 
    await callback.answer()

@dp.callback_query_handler(Text(startswith="description_hide"))
async def hide_description(callback: types.CallbackQuery):
    edit = await sql_db.sql_edit(callback.data.replace("description_hide ", ""))
    for i in edit:
        await bot.edit_message_text(
            f"Описание голосового: {i[3]}", 
            callback.from_user.id, 
            callback.message.message_id, 
            reply_markup=get_keyboard(i)
        )
    await callback.answer()

@dp.callback_query_handler(Text(startswith="description_delete"))
async def delete_description(callback: types.CallbackQuery):
    for i in range(callback.message.message_id - 1, callback.message.message_id + 1):
        await bot.delete_message(callback.from_user.id, i)
    await sql_db.sql_delete(callback.data.replace("description_delete ", ""))
    await callback.answer()

@dp.callback_query_handler(Text(startswith="description_back"))
async def back_to_menu(callback: types.CallbackQuery):
    if "База" in callback.message.text:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.delete_message(callback.from_user.id, callback.message.message_id - 1)
    await sort_by_tags.list_of_tags(callback)
    await callback.answer()

@dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(update, error):
    return True