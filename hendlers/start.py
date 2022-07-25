from asyncio import sleep

from loader import dp
from states.download import Download
from keyboards.default import find_kb
from aiogram import types


@dp.message_handler(commands=['start'])
async def start_work(message: types.Message):
    await message.answer("Привіт!")
    await sleep(0.5)
    await message.answer("Я бот який допоможе тобі завантажити твою улюблену музику в телеграм!")
    await sleep(0.5)
    await message.answer("Натискай 'Шукати' щоб почати роботу", reply_markup=find_kb)

    await Download.begin.set()
