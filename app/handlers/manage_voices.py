from aiogram import Router
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.dispatcher.filters import Text
from create import bot
from handlers.sort_by_tags import sort_tags, list_of_authors
from database.sql_db import sql_edit, sql_delete

router = Router()

amount = 0

def get_keyboard(i):
    global amount
    manage_keyboard = InlineKeyboardBuilder()
    manage_keyboard.row(
        InlineKeyboardButton(text="Посмотреть", callback_data=f"description_show {i[0]}"),
        InlineKeyboardButton(text="Удалить", callback_data=f"description_delete {i[0]}"),
        InlineKeyboardButton(text="Скрыть", callback_data=f"description_hide {i[0]}")
    )
    manage_keyboard.row(
        InlineKeyboardButton(text="⬅️", callback_data=f"tags_back"),
        InlineKeyboardButton(text=f"{amount + 1}/{len(sort_tags.read_tags)}", callback_data=f"tags_count"),
        InlineKeyboardButton(text="➡️", callback_data=f"tags_next")
    )
    manage_keyboard.add(
        InlineKeyboardButton(text="🔼Меню🔼", callback_data=f"menu")
    )
    manage_keyboard.adjust(3)
    return manage_keyboard.as_markup()

@router.callback_query(Text(text_startswith="description_show"))
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

@router.callback_query(Text(text_startswith="description_hide"))
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

@router.callback_query(Text(text_startswith="description_delete"))
async def delete_description(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await sql_delete(callback.data.replace("description_delete ", ""))
    await bot.send_message(callback.from_user.id, "Голосовое успешно удалено!\nВозвращаю вас в меню...")
    await list_of_authors(callback)
    await callback.answer()

@router.callback_query(text="tags_back")
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
        await callback.answer(cache_time=3)
    await callback.answer(cache_time=1)      

@router.callback_query(text="tags_count")
async def next_description(callback: CallbackQuery):
    await callback.answer(cache_time=1)

@router.callback_query(text="tags_next")
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
        await callback.answer(cache_time=3)
    await callback.answer(cache_time=1)

@router.callback_query(text="menu")
async def back_to_menu(callback: CallbackQuery):
    global amount
    amount = 0
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await list_of_authors(callback)
    await callback.answer()