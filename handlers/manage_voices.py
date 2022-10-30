from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified, MessageToDeleteNotFound
from create import dp, bot
from handlers.sort_by_tags import sort_tags, list_of_authors
from database.sql_db import sql_edit, sql_delete

amount = 0

def get_keyboard(i):
    global amount
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton(text="Посмотреть", callback_data=f"description_show {i[0]}"),
        InlineKeyboardButton(text="Скрыть", callback_data=f"description_hide {i[0]}"),
        InlineKeyboardButton(text="Удалить", callback_data=f"description_delete {i[0]}")
    ).row(
        InlineKeyboardButton(text="Назад", callback_data=f"tags_back"),
        InlineKeyboardButton(text=f"{amount + 1}/{len(sort_tags.read_tags)}", callback_data=f"tags_count"),
        InlineKeyboardButton(text="Вперед", callback_data=f"tags_next")
    ).add(InlineKeyboardButton(text="Меню", callback_data=f"menu")
    )

@dp.callback_query_handler(Text(startswith="description_show"))
async def show_description(callback: CallbackQuery):
    edit = await sql_edit(callback.data.replace("description_show ", ""))
    for i in edit:
        await bot.edit_message_caption( 
            callback.from_user.id, 
            callback.message.message_id, 
            caption = f"ID в базе данных: {i[0]}\nНазвание голосового: {i[2]}\nОписание голосового: {i[3]}\nТеги голосового: {i[4]}\nАвтор голосового: {i[5]}\nID Автора: {i[7]}",
            reply_markup=get_keyboard(i)
        ) 
    await callback.answer()

@dp.callback_query_handler(Text(startswith="description_hide"))
async def hide_description(callback: CallbackQuery):
    edit = await sql_edit(callback.data.replace("description_hide ", ""))
    for i in edit:
        await bot.edit_message_caption(
            callback.from_user.id, 
            callback.message.message_id,
            caption = f"Описание голосового: {i[3]}",
            reply_markup=get_keyboard(i)
        )
    await callback.answer()

@dp.callback_query_handler(text="tags_next")
async def next_description(callback: CallbackQuery):
    global amount
    amount += 1
    try:
        await bot.send_voice(
            callback.from_user.id, 
            sort_tags.read_tags[amount][1],
            f"Описание голосового: {sort_tags.read_tags[amount][3]}\n",
            reply_markup=get_keyboard(sort_tags.read_tags[amount])
        )
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
    except IndexError:
        amount -= 1
        return True
    await callback.answer()

@dp.callback_query_handler(text="tags_count")
async def next_description(callback: CallbackQuery):
    return True

@dp.callback_query_handler(text="tags_back")
async def next_description(callback: CallbackQuery):
    global amount
    amount -= 1
    try:
        if amount < 0:
            amount = 0
            return True
        else:
            await bot.send_voice(
                callback.from_user.id, 
                sort_tags.read_tags[amount][1],
                f"Описание голосового: {sort_tags.read_tags[amount][3]}\n", 
                reply_markup=get_keyboard(sort_tags.read_tags[amount])
            )
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
    except IndexError:
        return True
    await callback.answer()      

@dp.callback_query_handler(Text(startswith="description_delete"))
async def delete_description(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await sql_delete(callback.data.replace("description_delete ", ""))
    await bot.send_message(callback.from_user.id, "Голосовое успешно удалено!\nВозвращаю вас в меню...")
    await list_of_authors(callback)
    await callback.answer()

@dp.callback_query_handler(text="menu")
async def back_to_menu(callback: CallbackQuery):
    global amount
    amount = 0
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await list_of_authors(callback)
    await callback.answer()

@dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(update, error):
    return True

@dp.errors_handler(exception=MessageToDeleteNotFound)
async def message_not_modified_handler(update, error):
    return True