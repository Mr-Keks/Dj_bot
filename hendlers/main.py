from asyncio import sleep

from loader import dp, bot
from states.download import Download
from dw import Audio
from keyboards import default
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=Download.begin)
async def get_url(message: types.Message):
    await message.answer("Надішли мені посилання на пісню, яку ти хочеш завантажити")
    await Download.url.set()


@dp.message_handler(state=Download.url)
async def find_music(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['url'] = message.text
    await message.answer("Зараз спробую знайти!")

    url_data = await state.get_data()
    audio = Audio(url_data.get('url'))

    if audio.check_url():
        await message.answer('Я знайшов!')
        await sleep(0.3)
        await message.answer('Зачекай трішки, це може зайняти деякий час')

        audio.download_video()
        audio.convert_to_mp3()

        await message.answer("Ось, насолоджуйся :)")
        await sleep(0.1)

        print('before')
        #await bot.send_audio(message.from_user.id, audio=audio.file)
        await message.answer_audio(audio=audio.file)
        print('end')

        await state.finish()

    else:
        await message.answer("Я нажаль не можу знайти нічого за цією адресою(", reply_markup=default.failTry_kb)

        if message.text == "Шукати знову":
            await Download.begin.set()
        else:
            await state.finish()
            await message.answer("Можливо пощастить наступного разу!")


