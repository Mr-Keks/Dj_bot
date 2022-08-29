from aiogram import Dispatcher

from . import throttlingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(throttlingMiddleware.ThrottlingMiddleware())