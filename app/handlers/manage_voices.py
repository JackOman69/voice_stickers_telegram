from aiogram import Router
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.dispatcher.filters import Text
from create import bot
from handlers.sort_by_tags import sort_tags, list_of_authors
import httpx

router = Router()
amount = 0

def get_keyboard(id):
    global amount, len_voices
    manage_keyboard = InlineKeyboardBuilder()
    manage_keyboard.row(
        InlineKeyboardButton(text="Посмотреть", callback_data=f"description_show {id}"),
        InlineKeyboardButton(text="Удалить", callback_data=f"description_delete {id}"),
        InlineKeyboardButton(text="Скрыть", callback_data=f"description_hide {id}")
    )
    manage_keyboard.row(
        InlineKeyboardButton(text="⬅️", callback_data=f"tags_back"),
        InlineKeyboardButton(text=f"{amount + 1}/{len(sort_tags.voices_by_tags) }", callback_data=f"tags_count"),
        InlineKeyboardButton(text="➡️", callback_data=f"tags_next")
    )
    manage_keyboard.add(
        InlineKeyboardButton(text="🔼Меню🔼", callback_data=f"menu")
    )
    manage_keyboard.adjust(3)
    return manage_keyboard.as_markup()

@router.callback_query(Text(text_startswith="description_show"))
async def show_description(callback: CallbackQuery):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://api/bot/id/?id=" + callback.data.replace("description_show ", ""))
        show_data_voice = response.json() 
    await bot.edit_message_caption( 
        callback.from_user.id, 
        callback.message.message_id, 
        caption = "ID в базе данных: " + str(show_data_voice["id"]) + "\n" + "Название голосового: " + show_data_voice["name"] + "\n" + "Описание голосового: " + show_data_voice["description"] + "\n" + "Теги голосового: " + ", ".join(show_data_voice["tags"]) + "\n" + "Автор голосового: " + show_data_voice["author"] + "\n" + "ID Автора: " + str(show_data_voice["admin_author_id"]),
        reply_markup=get_keyboard(show_data_voice["id"])
    ) 
    await callback.answer()

@router.callback_query(Text(text_startswith="description_hide"))
async def hide_description(callback: CallbackQuery):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://api/bot/id/?id=" + callback.data.replace("description_hide ", ""))
        hide_data_voice = response.json() 
    await bot.edit_message_caption(
        callback.from_user.id, 
        callback.message.message_id,
        caption = "Описание голосового: " + hide_data_voice["description"],
        reply_markup=get_keyboard(hide_data_voice["id"])
    )
    await callback.answer()

@router.callback_query(Text(text_startswith="description_delete"))
async def delete_description(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    async with httpx.AsyncClient() as client:
        await client.delete("http://api/bot/delete/?id=" + callback.data.replace("description_delete ", ""))
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
                sort_tags.voices_by_tags[amount]["voice"],
                "Описание голосового: " + sort_tags.voices_by_tags[amount]["description"] + "\n", 
                reply_markup=get_keyboard(sort_tags.voices_by_tags[amount]["id"])
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
            sort_tags.voices_by_tags[amount]["voice"],
            "Описание голосового: " + sort_tags.voices_by_tags[amount]["description"] + "\n",
            reply_markup=get_keyboard(sort_tags.voices_by_tags[amount]["id"])
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