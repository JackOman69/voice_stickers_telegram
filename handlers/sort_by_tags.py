from aiogram import types
from aiogram.dispatcher.filters import Text
from create import dp, bot
from handlers import manage_voices
from database import sql_db

def sort_keyboard(tags):
    tags_inline = []
    for i in tags:
        tags_inline.append(types.InlineKeyboardButton(text=i, callback_data=f"sort_by_tags {i}"))
    return types.InlineKeyboardMarkup(inline_keyboard=[[i] for i in tags_inline])

async def delete_messages(message):
    if message.message_id + 1:
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)

@dp.callback_query_handler(Text(startswith="sort_by_tags"))
async def sort_tags(callback: types.CallbackQuery):
    read = await sql_db.sql_sort_by_tags(callback.data.replace("sort_by_tags ", ""))
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    for i in read:
        await bot.send_voice(callback.from_user.id, i[1])
        await bot.send_message(
            callback.from_user.id, 
            f"Описание голосового: {i[3]}\n", 
            reply_markup=manage_voices.get_keyboard(i)
        )
    await callback.answer()

async def list_of_tags(message: types.Message):
    read_tags = await sql_db.sql_read_tags()    
    tags = list(set([i[j] for i in [i[0].split(", ") for i in read_tags] for j in range(len(i))]))
    if not tags:
        return await bot.send_message(message.from_user.id, "База данных пуста!")
    await bot.send_message(
        message.from_user.id, 
        "Выберете тэг голосового, который хотите посмотреть:", 
        reply_markup = sort_keyboard(tags)
    )
    # await delete_messages(message)

def database_handler(dp):
    dp.register_message_handler(list_of_tags, commands=["База данных"])
    dp.register_message_handler(list_of_tags, Text(equals="база данных", ignore_case=True))