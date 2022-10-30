from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from create import bot
from keyboard import kb_admin, kb_start
from database.sql_db import sql_add

ADMIN_ID = [509237723, 458554554, 440280067]

class FSMVoices(StatesGroup):
    voice, name, description, tags, author = State(), State(), State(), State(), State()

async def delete_messages(message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.delete_message(message.from_user.id, message.message_id - 1)

async def cancel_handler(message: Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Вы успешно отменили операцию!", reply_markup=kb_start.kb_menu)
    await delete_messages(message)

async def add_start(message: Message, state=None):
    if message.from_user.id in ADMIN_ID:
        await FSMVoices.voice.set()
        await message.answer("Здраствуй, админ!\nДля начала пришли голосовое:", reply_markup=kb_admin.kb_cancel)
        await delete_messages(message)

async def add_voice(message: Message, state=FSMContext):
    if message.from_user.id in ADMIN_ID:
        async with state.proxy() as data:
            data["voice"] = message.voice.file_id
        await FSMVoices.next()
        await message.answer("Добавь название голосового:")
        await delete_messages(message)

async def add_name(message: Message, state=FSMContext):
    if message.from_user.id in ADMIN_ID:
        async with state.proxy() as data:
            data["name"] = message.text
        await FSMVoices.next()
        await message.answer("Добавь описание голосового:")
        await delete_messages(message)

async def add_description(message: Message, state=FSMContext):
    if message.from_user.id in ADMIN_ID:
        async with state.proxy() as data:
            data["description"] = message.text
        await FSMVoices.next()
        await message.answer("Добавь теги голосового через запятую:")
        await delete_messages(message)

async def add_tags(message: Message, state=FSMContext):
    if message.from_user.id in ADMIN_ID:
        async with state.proxy() as data:
            data["tags"] = message.text.lower()
        await FSMVoices.next()
        await message.answer("Добавь имя автора голосового:")
        await delete_messages(message)        

async def add_author_and_id(message: Message, state=FSMContext):
    if message.from_user.id in ADMIN_ID:
        async with state.proxy() as data:
            data["author"] = message.text.title()
            data["admin_author_id"] = message.from_user.id
        await message.answer("Далее в базу автоматически вставится ваш ID...") 
        await sql_add(state)
        await message.answer("Готово!", reply_markup=kb_start.kb_menu)
        await delete_messages(message)
        await state.finish()  

def register_voices(dp):
    dp.register_message_handler(cancel_handler, commands=["Отмена"],state="*")
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(add_start, commands=["Загрузить"], state=None)
    dp.register_message_handler(add_start, Text(equals="загрузить", ignore_case=True), state=None)
    dp.register_message_handler(add_voice, content_types=[ContentType.VOICE], state=FSMVoices.voice)
    dp.register_message_handler(add_name, state=FSMVoices.name)
    dp.register_message_handler(add_description, state=FSMVoices.description)
    dp.register_message_handler(add_tags, state=FSMVoices.tags)
    dp.register_message_handler(add_author_and_id, state=FSMVoices.author)