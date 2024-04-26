import logging

from aiogram import Bot, Dispatcher
import asyncio

from callbacks import ready_resume
from core.config import settings
from core.constants import HTML, RQUID
from gigachat import GigaChat
from handlers import bot_messagers, user_commands
from keyboards.main_menu import set_main_menu

bot = Bot(token=settings.telegram_token, parse_mode=HTML,)
chat = GigaChat(settings.authorization, RQUID,)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_routers(
        user_commands.router,
        ready_resume.router,
        bot_messagers.router,
    )
    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True,)
    await dp.start_polling(bot,)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
