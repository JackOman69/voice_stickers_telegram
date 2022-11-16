from aiogram import Router
from aiogram.types import InlineKeyboardButton, CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.dispatcher.filters import Text
from create import bot
from handlers import manage_voices
import httpx
from create import ADMINS

router = Router()

def sort_author_keyboard(authors):
    builder_authors = InlineKeyboardBuilder()
    for i in authors:
        builder_authors.add(InlineKeyboardButton(text=i, callback_data=f"sort_voices_authors {i}"))
    builder_authors.adjust(1)
    return builder_authors.as_markup()

def sort_tags_keyboard(sorted_tags):
    builder_tags = InlineKeyboardBuilder()
    for i in sorted_tags:
        builder_tags.add(InlineKeyboardButton(text=i, callback_data=f"sort_voices_tags {i}"))
    builder_tags.add(InlineKeyboardButton(text="🔼Меню🔼", callback_data=f"menu"))
    builder_tags.adjust(1)
    return builder_tags.as_markup()

@router.message(commands=["База данных"])
@router.message(Text(text="база данных", text_ignore_case=True))
async def list_of_authors(message: Message):
    if message.from_user.id in ADMINS:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://api/bot/authors/all")
            read_authors = response.json()
        authors = list(set([i["author"] for i in read_authors]))
        if not authors:    
            await bot.send_message(message.from_user.id, "База данных пуста!")
            return
        await bot.send_message(
            message.from_user.id, 
            "Выберите автора голосового, чьи теги вы хотите посмотреть:", 
            reply_markup = sort_author_keyboard(authors)
        )

@router.callback_query(Text(text_startswith="sort_voices_authors"))
async def list_of_tags(callback: CallbackQuery):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://api/bot/tags/sorted?author=" + callback.data.replace("sort_voices_authors ", ""))
        read_tags_by_authors = response.json()
    sorted_tags_by_authors = list(set([j for i in read_tags_by_authors for j in i["tags"]]))
    await bot.edit_message_text(
        "Выберите тег голосового, который хотите посмотреть:",
        callback.from_user.id, 
        callback.message.message_id, 
    )
    await bot.edit_message_reply_markup(
        callback.from_user.id, 
        callback.message.message_id,
        reply_markup = sort_tags_keyboard(sorted_tags_by_authors) 
    )
    await callback.answer()

@router.callback_query(Text(text_startswith="sort_voices_tags"))
async def sort_tags(callback: CallbackQuery):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://api/bot/tags/?tag=" + callback.data.replace("sort_voices_tags ", ""))
        sort_tags.voices_by_tags = response.json()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_voice(
        callback.from_user.id, 
        sort_tags.voices_by_tags[0]["voice"],
        "Описание голосового: " + sort_tags.voices_by_tags[0]["description"] + "\n",
        reply_markup=manage_voices.get_keyboard(sort_tags.voices_by_tags[0]["id"])
    )
    await callback.answer()
