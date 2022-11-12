from aiogram import Router
from aiogram.types import Message
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from create import bot
from keyboard import kb_admin, kb_start
from database.sql_db import sql_add
from create import ADMINS


router = Router()

class FSMVoices(StatesGroup):
    voice, name, description, tags, author = State(), State(), State(), State(), State()

async def delete_messages(message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.delete_message(message.from_user.id, message.message_id - 1)

@router.message(commands=["Отмена"])
@router.message(Text(text="отмена", text_ignore_case=True))
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("Вы успешно отменили операцию!", reply_markup=kb_start.kb_menu)
    await delete_messages(message)

@router.message(commands=["Загрузить"])
@router.message(Text(text="загрузить", text_ignore_case=True))
async def add_start(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.set_state(FSMVoices.voice)
        await message.answer("Здраствуй, админ!\nДля начала пришли голосовое:", reply_markup=kb_admin.kb_cancel)
        await delete_messages(message)

@router.message(FSMVoices.voice)
async def add_voice(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(voice=message.voice.file_id)
        await state.set_state(FSMVoices.name)
        await message.answer("Добавь название голосового:")
        await delete_messages(message)

@router.message(FSMVoices.name)
async def add_name(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(name=message.text)
        await state.set_state(FSMVoices.description)
        await message.answer("Добавь описание голосового:")
        await delete_messages(message)

@router.message(FSMVoices.description)
async def add_description(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(description=message.text)
        await state.set_state(FSMVoices.tags)
        await message.answer("Добавь теги голосового через запятую:")
        await delete_messages(message)

@router.message(FSMVoices.tags)
async def add_tags(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(tags=message.text.lower())
        await state.set_state(FSMVoices.author)
        await message.answer("Добавь имя автора голосового:")
        await delete_messages(message)        

@router.message(FSMVoices.author)
async def add_author_and_id(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(author=message.text.lower())
        await state.update_data(admin_author_id=message.from_user.id)
        await message.answer("Далее в базу автоматически вставится ваш ID...") 
        await sql_add(state)
        await message.answer("Готово!", reply_markup=kb_start.kb_menu)
        await delete_messages(message)
        await state.clear()
