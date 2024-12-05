import logging

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.models.common import Users
from app.services.auth import is_registered
from app.services.common import get_function_name
from internal.database import get_session
from internal.config import config

router = Router()

class RegistrationStates(StatesGroup):
    await_name = State()
    await_surname = State()


@router.callback_query(F.data == "register")
async def register_command(callback_query: CallbackQuery, state: FSMContext):
    try:
        if is_registered(callback_query.from_user.id):
            await callback_query.answer(config["answers"]["user_is_registered"])
            return
        await callback_query.message.answer("Здорово, что решили к нам присоединиться!\nНапишите Ваше имя")
        await callback_query.answer()
        await state.set_state(RegistrationStates.await_name)
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")


@router.message(RegistrationStates.await_name)
async def process_name(message: Message, state: FSMContext):
    try:
        await state.update_data(name=message.text)
        await state.set_state(RegistrationStates.await_surname)
        await message.answer("Напишите Вашу фамилию")
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")
    
    
@router.message(RegistrationStates.await_surname)    
async def process_surname(message: Message, state: FSMContext):
    try:
        await state.update_data(surname=message.text)
        data = await state.get_data()
        with get_session() as session:
            session.add(Users(telegram_id=message.from_user.id, name=data["name"], surname=data["surname"]))
            session.commit()
        await message.answer("Регистрация прошла успешно!")
        await state.clear()
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")
