from aiogram import Router
from aiogram.types import InlineKeyboardButton, CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.dispatcher.filters import Text
from create import bot
from handlers import manage_voices
from database import sql_db
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

def sorted_list(sorting):
    return list(set([i[j] for i in [i[0].split(", ") for i in sorting] for j in range(len(i))]))

@router.message(commands=["База данных"])
@router.message(Text(text="база данных", text_ignore_case=True))
async def list_of_authors(message: Message):
    if message.from_user.id in ADMINS:
        read_authors = await sql_db.sql_read_author()    
        authors = sorted_list(read_authors)
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
    sort_tags_by_authors = await sql_db.sql_sort_by_authors(callback.data.replace("sort_voices_authors ", ""))
    sorted_tags = sorted_list(sort_tags_by_authors)
    await bot.edit_message_text(
        "Выберите тег голосового, который хотите посмотреть:",
        callback.from_user.id, 
        callback.message.message_id, 
    )
    await bot.edit_message_reply_markup(
        callback.from_user.id, 
        callback.message.message_id,
        reply_markup = sort_tags_keyboard(sorted_tags) 
    )
    await callback.answer()

@router.callback_query(Text(text_startswith="sort_voices_tags"))
async def sort_tags(callback: CallbackQuery):
    sort_tags.read_tags = await sql_db.sql_sort_by_tags(callback.data.replace("sort_voices_tags ", ""))
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_voice(
        callback.from_user.id, 
        sort_tags.read_tags[0][1], 
        f"Описание голосового: {sort_tags.read_tags[0][3]}\n", 
        reply_markup=manage_voices.get_keyboard(sort_tags.read_tags[0])
    )
    await callback.answer()
