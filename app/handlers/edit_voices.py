from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboard import kb_cancel, kb_start
from create import bot
from handlers.sort_by_tags import list_of_authors
import httpx
import json

router = Router()

class FSMEdit(StatesGroup):
    name, description, tags, author = State(), State(), State(), State()
    
url = ""

@router.callback_query(Text(text_startswith="description_edit"))
async def delete_description(callback: CallbackQuery, state: FSMContext):
    global url
    url = "http://api/bot/edit/?id=" + callback.data.replace("description_edit ", "")
    await state.set_state(FSMEdit.name)
    await bot.send_message(callback.from_user.id, "Напишите изменения для названия голосового:", reply_markup=kb_cancel.kb_cancel)
    await callback.answer()
    
@router.message(FSMEdit.name)
async def edit_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FSMEdit.description)
    await bot.delete_message(message.from_user.id, message.message_id - 1)
    await message.answer("Напишите изменения для описания голосового:")
    
@router.message(FSMEdit.description)
async def edit_name(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(FSMEdit.tags)
    await bot.delete_message(message.from_user.id, message.message_id - 1)
    await message.answer("Напишите изменения для тегов голосового через запятую:")

@router.message(FSMEdit.tags)
async def edit_name(message: Message, state: FSMContext):
    await state.update_data(tags=message.text.lower().split(", "))
    await state.set_state(FSMEdit.author)
    await bot.delete_message(message.from_user.id, message.message_id - 1)
    await message.answer("Напишите изменения для автора голосового:")

@router.message(FSMEdit.author)
async def edit_name(message: Message, state: FSMContext):
    global url
    await state.update_data(author=message.text)
    dict_data = await state.get_data()
    json_data = json.dumps(dict_data, ensure_ascii=False)
    async with httpx.AsyncClient() as client:
        await client.put(url, data = json_data)
    await state.clear()
    await bot.delete_message(message.from_user.id, message.message_id - 1)
    await message.answer("Голосовое успешно обновлено!\nВозвращаю вас в меню...", reply_markup=kb_start.kb_menu)
    await list_of_authors(message)
    