from aiogram import types, Router
from aiogram.filters import Command

from core.constants import GREETING, HELP_TEXT, HELP_MAKE_RESUME
import main

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(
        GREETING,
    )
    text = main.chat.ask_a_question(HELP_MAKE_RESUME,)
    await message.answer(text,)


@router.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer(
        HELP_TEXT,
    )
