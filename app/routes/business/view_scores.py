import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from app.models.common import Scores, Users
from app.services.auth import is_registered
from app.services.common import get_function_name
from internal.database import get_session
from internal.config import config

router = Router()


@router.callback_query(F.data == "view_scores")
async def view_scores(callback_query: CallbackQuery, state: FSMContext):
    try:
        with get_session() as session:
            user_scores = session.query(Scores).filter(Scores.telegram_id == callback_query.from_user.id).all()
        if user_scores == []:
            await callback_query.message.answer("Вы не внесли результаты ЕГЭ")
            await callback_query.answer()
            return
        message = "Результаты ЕГЭ:\n\n"
        for i in user_scores:
            message += f"{i.discipline}: {i.score}\n"
        await callback_query.message.answer(message)
        await callback_query.answer()
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")


@router.message(Command("view_scores"))
async def view_scores_command(message: Message, state: FSMContext):
    try:
        if not is_registered(message.from_user.id):
            await message.answer(config["answers"]["user_is_not_registered"])
            return
        with get_session() as session:
            user_scores = session.query(Scores).filter(Scores.telegram_id == message.from_user.id).all()
        if user_scores == []:
            await message.answer("Вы не внесли результаты ЕГЭ")
            return
        message_text = "Результаты ЕГЭ:\n\n"
        for i in user_scores:
            message_text += f"{i.discipline}: {i.score}\n"
        await message.answer(message_text)
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")
    