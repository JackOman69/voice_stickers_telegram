from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv 
import os

load_dotenv(find_dotenv())

ADMINS = [int(i) for i in os.getenv("ADMIN_ID").split(",")]

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(storage=MemoryStorage())