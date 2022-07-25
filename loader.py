from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='5239702184:AAHEj4XN_kffWyrxZ7zKXp9iigzMLyc4WK4')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
