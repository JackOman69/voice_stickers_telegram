from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboard import kb_client

ADMIN_ID = 2014604156

class FSMAdmin(StatesGroup):
    photo, name, description, rarity = State(), State(), State(), State()

async def is_admin(message: types.Message):
    global ADMIN_ID
    if message.from_user.id == ADMIN_ID:
        await message.answer("Здраствуй, главный шизик")
    else:
        await message.answer("Ты не главный шизик!!! Пошел к черту!")

async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.answer("Для начала фоточку ублюдыша:")

async def cancel_handler(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Хорошо")

async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Теперь имя шизика:")

async def load_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMAdmin.next()
    await message.answer("Описание ублюдыша: кто такой, кто по жизни, почему шизит")

async def load_description(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text
    await FSMAdmin.next()
    await message.answer("Присвой редкость этому ублюдышу через клавиатурку(ДЛЯ ТУПЫХ)", reply_markup=ReplyKeyboardRemove())

async def load_rariry(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["rarity"] = message.text
    async with state.proxy() as data:
        await message.answer(str(data))
    await state.finish()

def add_shiz(dp: Dispatcher):
    dp.register_message_handler(is_admin, commands=["Админ"], state=None)
    dp.register_message_handler(cm_start, commands=["Загрузить"], state=None)
    dp.register_message_handler(cancel_handler, commands=["Отмена"],state="*")
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=["photo"], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_rariry, state=FSMAdmin.rarity)
