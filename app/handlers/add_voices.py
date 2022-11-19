from aiogram import Router
from aiogram.types import Message
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from create import bot
from create import ADMINS
from handlers.sort_by_tags import list_of_authors
from keyboard import kb_cancel, kb_start
import httpx
import json


router = Router()

class FSMVoices(StatesGroup):
    voice, name, description, tags, author, admin_author_id = State(), State(), State(), State(), State(), State()

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
        await message.answer("Здраствуй, админ!\nДля начала пришли голосовое:", reply_markup=kb_cancel.kb_cancel)

@router.message(FSMVoices.voice)
async def add_voice(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(voice=message.voice.file_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        await state.set_state(FSMVoices.name)
        await message.answer("Добавь название голосового:")

@router.message(FSMVoices.name)
async def add_name(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(name=message.text)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        await state.set_state(FSMVoices.description)
        await message.answer("Добавь описание голосового:")

@router.message(FSMVoices.description)
async def add_description(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(description=message.text)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        await state.set_state(FSMVoices.tags)
        await message.answer("Добавь теги голосового через запятую:")

@router.message(FSMVoices.tags)
async def add_tags(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(tags=message.text.lower().split(", "))
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        await state.set_state(FSMVoices.author)
        await message.answer("Добавь имя автора голосового:")      

@router.message(FSMVoices.author)
async def add_author_and_id(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(author=message.text.capitalize())
        await state.update_data(admin_author_id=message.from_user.id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        await message.answer("Далее в базу автоматически вставится ваш ID...")
        dict_data = await state.get_data()
        json_data = json.dumps(dict_data, ensure_ascii=False)
        print(json_data)
        async with httpx.AsyncClient() as client:
            await client.post("http://api/bot/create/", data=json_data)
        await state.clear()
        await message.answer("Голосовое сообщение добавлено в базу данных!\nВозвращаю вас в меню...", reply_markup=kb_start.kb_menu)
        await list_of_authors(message)
