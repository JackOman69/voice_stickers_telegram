from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

API_TOKEN = "5667475318:AAERzM5rl2Xui0hvC01QWp5p3zfxmPrjxuo"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)