import logging

from aiogram import executor
from aiogram.utils.executor import start_webhook

from loader import dp, WEBHOOK_URL, WEBAPP_HOST, WEBHOOK_PATH, WEBAPP_PORT, bot

logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    import hendlers
    import middlewares

    hendlers.setup(dp)
    middlewares.setup(dp)

    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dp):
    await bot.delete_webhook()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
