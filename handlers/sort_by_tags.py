from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.dispatcher.filters import Text
from create import bot, dp
from handlers import manage_voices
from database import sql_db

def sort_author_keyboard(authors):
    authors_inline = []
    for i in authors:
        authors_inline.append(InlineKeyboardButton(text=i, callback_data=f"sort_voices_authors {i}"))
    return InlineKeyboardMarkup(inline_keyboard=[[i] for i in authors_inline])

def sort_tags_keyboard(sorted_tags):
    tags_inline = []
    for i in sorted_tags:
        tags_inline.append(InlineKeyboardButton(text=i, callback_data=f"sort_voices_tags {i}"))
    return InlineKeyboardMarkup(inline_keyboard=[[i] for i in tags_inline]).add(InlineKeyboardButton(text="Меню", callback_data=f"menu"))

def sorted_list(sorting):
    return list(set([i[j] for i in [i[0].split(", ") for i in sorting] for j in range(len(i))]))

@dp.callback_query_handler(Text(startswith="sort_voices_tags"))
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

@dp.callback_query_handler(Text(startswith="sort_voices_authors"))
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

async def list_of_authors(message: Message):
    read_authors = await sql_db.sql_read_author()    
    authors = sorted_list(read_authors)
    if not authors:    
        await bot.send_message(message.from_user.id, "База данных пуста!")
    await bot.send_message(
        message.from_user.id, 
        "Выберите автора голосового, чьи теги вы хотите посмотреть:", 
        reply_markup = sort_author_keyboard(authors)
    )

def database_handler(dp):
    dp.register_message_handler(list_of_authors, commands=["База данных"])
    dp.register_message_handler(list_of_authors, Text(equals="база данных", ignore_case=True))