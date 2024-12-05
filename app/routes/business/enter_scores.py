import logging

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.filters import Command, StateFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.models.common import Scores
from app.services.auth import is_registered
from app.services.common import get_function_name
from internal.database import get_session
from internal.config import config

router = Router()

class EnterScoresStates(StatesGroup):
    await_discipline = State()
    await_score = State()


@router.callback_query(F.data == "enter_scores")
async def enter_discipline(callback_query: CallbackQuery, state: FSMContext):
    try:
        builder = InlineKeyboardBuilder()
        for i in config["disciplines"]:
            builder.button(text=i, callback_data=f"enter_scores_{i}")
        builder.adjust(2)
        await state.set_state(EnterScoresStates.await_discipline)
        await callback_query.message.answer("Выберите дисциплину:", reply_markup=builder.as_markup())
        await callback_query.answer()
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")


@router.message(Command("enter_scores"))
async def enter_scores_command(message: Message, state: FSMContext):
    try:
        if not is_registered(message.from_user.id):
            await message.answer(config["answers"]["user_is_not_registered"])
            return
        builder = InlineKeyboardBuilder()
        for i in config["disciplines"]:
            builder.button(text=i, callback_data=f"enter_scores_{i}")
        builder.adjust(2)
        await state.set_state(EnterScoresStates.await_discipline)
        await message.answer("Выберите дисциплину:", reply_markup=builder.as_markup())
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")


@router.callback_query(F.data.startswith("enter_scores_"), StateFilter(EnterScoresStates.await_discipline))
async def enter_scores(callback_query: CallbackQuery, state: FSMContext):
    try:
        await state.update_data(discipline=callback_query.data[len("enter_scores_"):])
        await state.set_state(EnterScoresStates.await_score)
        await callback_query.message.answer("Введите количество баллов")
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")


@router.message(StateFilter(EnterScoresStates.await_score))
async def enter_score(message: Message, state: FSMContext):
    try:
        await state.update_data(score=message.text)
        data = await state.get_data()
        await state.clear()
        with get_session() as session:
            # если результат с этой дисциплиной уже есть, обновляем, если нет, создаем новую запись
            score_in_db = session.query(Scores).filter(Scores.telegram_id == message.from_user.id, Scores.discipline == data["discipline"]).first()
            if score_in_db:
                score_in_db.score = data["score"]
            else:
                session.add(Scores(telegram_id=message.from_user.id, discipline=data["discipline"], score=data["score"]))
            session.commit()
        await message.answer("Результат добавлен!")
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")
    

