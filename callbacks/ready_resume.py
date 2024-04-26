from aiogram import F, Router, types

from core.constants import RESTART_RESUME, SATISFIED_RESUME, TEXT_START_OVER
from keyboards.kb_gigachat import restart_resume
from handlers.user_commands import cmd_start
import main


router = Router()


@router.callback_query(F.data == SATISFIED_RESUME)
async def resume_callback(
    callback_query: types.CallbackQuery,
):
    """Отправляет составленное резюме и удаляет все сообщения с ботом."""
    await callback_query.message.answer(
        main.chat.communication[-3]['content'],
        )
    main.chat.reset()
    await callback_query.message.answer(
        TEXT_START_OVER,
        reply_markup=restart_resume,
    )


@router.callback_query(F.data == RESTART_RESUME)
async def restart_resume_callback(
    callback_query: types.CallbackQuery,
):
    """Начинает заново составлять резюме."""
    await cmd_start(callback_query.message,)
