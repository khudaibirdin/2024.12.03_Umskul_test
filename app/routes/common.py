import logging

from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.models.common import Users
from app.services.auth import is_registered
from app.services.common import get_function_name
from internal.database import get_session
from internal.config import config

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):  
    """
    Обработчик команды /start
    """
    try:
        builder = InlineKeyboardBuilder()
        # если не зарегистрирован, предлагаем регистрацию
        if not is_registered(message.from_user.id):
            builder.button(text="Регистрация", callback_data="register")
            photo = FSInputFile("static/images/icon.png")
            await message.answer_photo(photo, caption=config["answers"]["start_if_not_registered"], reply_markup=builder.as_markup())
        else:
            builder.button(text="Добавить результаты ЕГЭ", callback_data="enter_scores")
            builder.button(text="Показать результаты ЕГЭ", callback_data="view_scores")
            with get_session() as session:
                user = session.query(Users).filter(Users.telegram_id == message.from_user.id).first()
            await message.answer(f"Привет, {user.name}! 💯\nЭто бот сервиса сбора баллов ЕГЭ для учеников!\nВыбери интересующий пункт:", reply_markup=builder.as_markup())
    except Exception as e:
        logging.error(f"func: {get_function_name()}; error: {e}")