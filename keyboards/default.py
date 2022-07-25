from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard import KeyboardButton

find_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Шукати')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True)


failTry_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Шукати знову'),
            KeyboardButton(text='Завершити')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)