from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from core.constants import (
    GET_RESUME, RESTART_RESUME, SATISFIED_RESUME, START_OVER,
)
satisfied_resume = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=GET_RESUME,
                callback_data=SATISFIED_RESUME,
            ),
        ],
    ],
)

restart_resume = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=START_OVER,
                callback_data=RESTART_RESUME,
            ),
        ],
    ],
)
