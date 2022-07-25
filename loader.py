from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from environs import Env

env = Env()
env.read_env()

bot = Bot(token=env('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
