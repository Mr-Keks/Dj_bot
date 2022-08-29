from asyncio import sleep

from loader import dp
from states.download import Download
from keyboards.default import find_kb
from aiogram import types
from utils.misc.throttling import rate_limit

@dp.message_handler(commands=['start'])
@rate_limit(1)
async def start_work(message: types.Message):
    await message.answer("Привіт!")
    await sleep(0.5)
    await message.answer("Я бот який допоможе тобі завантажити твою улюблену музику з ютубу в телеграм!")
    await sleep(0.5)
    await message.answer("Натискай 'Шукати' щоб почати роботу", reply_markup=find_kb)

    await Download.begin.set()
