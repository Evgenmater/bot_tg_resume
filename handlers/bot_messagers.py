import uuid

from aiogram import types, F, Router


from core.constants import (
    ADD_TO_RESUME, TEXT_GET_A_RESUME, PROCESSING_REQUEST, WHAT_ADD_RESUME
)
from keyboards.kb_gigachat import satisfied_resume
import main
from speechflow import speech_to_text


router = Router()


@router.message(F.content_type == 'voice')
async def voice_processing(message: types.Message):
    """Обработка голосовых сообщений."""
    await message.answer(PROCESSING_REQUEST,)

    file_name = f'.{str(uuid.uuid4())}.mp3'
    file_info = await main.bot.get_file(message.voice.file_id)
    await main.bot.download_file(file_info.file_path, file_name,)
    result = [res async for res in speech_to_text(file_name)]

    text_for_gigachat = main.chat.ask_a_question(
        f'{ADD_TO_RESUME} {result[0]}',
    )
    await message.answer(text_for_gigachat,)

    can_add_my_resume = main.chat.ask_a_question(WHAT_ADD_RESUME,)
    await message.answer(
        f'{can_add_my_resume} {TEXT_GET_A_RESUME}',
        reply_markup=satisfied_resume,
    )


@router.message()
async def text_processing(message: types.Message):
    """Обработка остальных сообщений."""
    await message.answer(PROCESSING_REQUEST)
    text_for_gigachat = main.chat.ask_a_question(
        f'{ADD_TO_RESUME} {message.text}'
    )
    await message.answer(text_for_gigachat,)

    can_add_my_resume = main.chat.ask_a_question(WHAT_ADD_RESUME,)
    await message.answer(
        f'{can_add_my_resume} {TEXT_GET_A_RESUME}',
        reply_markup=satisfied_resume,
    )
