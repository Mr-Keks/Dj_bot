from asyncio import sleep

from loader import dp
from states.download import Download
from dw import Audio, check_url
from keyboards import default
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=Download.begin)
@dp.message_handler(text=["Шукати знову", "Шукати"])
async def get_url(message: types.Message):
    await message.answer("Надішли мені посилання на пісню, яку ти хочеш завантажити")
    await Download.url.set()


@dp.message_handler(state=Download.url)
async def find_music(message: types.Message, state: FSMContext):
    await message.answer("Зараз спробую знайти!")
    await sleep(0.5)
    await check_url_validation(message, message.text)
    await state.finish()


async def check_url_validation(message: types.Message, url: str):
    yt, mp4 = await check_url(url)
    if yt:
        await download_music(message, yt, mp4)
    else:
        await fail_try(message)


async def download_music(message: types.Message, yt, mp4):
    await message.answer('Я знайшов!')
    await sleep(0.5)
    await message.answer('Зачекай трішки, це може зайняти декілька секунд')

    audio = Audio(yt, mp4)
    res, title = await audio.download_video()

    await message.answer("Ось, насолоджуйся :)")
    await sleep(0.1)

    await message.answer_audio(audio=res, reply_markup=default.failTry_kb, title=title)


async def fail_try(message: types.Message):
    await message.answer("Я нажаль не можу знайти нічого за цією адресою(", reply_markup=default.failTry_kb)
