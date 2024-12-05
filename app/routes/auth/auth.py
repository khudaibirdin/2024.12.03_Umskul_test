# from aiogram import Router, F
# from aiogram.types import Message, CallbackQuery
# from aiogram.filters import Command
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext

# from app.services.auth import is_authenticated
# from app.models.common import Users
# from internal.database import get_session

# router = Router()


# class AuthentificationStates(StatesGroup):
#     await_name = State()
#     await_surname = State()


# @router.callback_query(F.data == "auth")
# async def auth_command(callback_query: CallbackQuery, state: FSMContext):
#     if not is_authenticated(callback_query.from_user.id):
#         await callback_query.message.answer("\nНапишите Ваше имя")
#         await callback_query.answer()
#         await state.set_state(AuthentificationStates.await_name) 
#     else:
#         await callback_query.answer("Вы уже авторизованы")


# @router.message(AuthentificationStates.await_name)
# async def process_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(AuthentificationStates.await_surname)
#     await message.answer("Напишите Вашу фамилию")


# @router.message(AuthentificationStates.await_surname)
# async def process_surname(message: Message, state: FSMContext):
#     await state.update_data(surname=message.text)
#     data = await state.get_data()
#     with get_session() as session:
#         # если пользователь авторизован, то дизавторизуем
#         user_in_db = session.query(Users).filter(Users.telegram_id == message.from_user.id, Users.is_authenticated == True).first()
#         if user_in_db:
#             user_in_db.is_authenticated = False
#             session.commit()
#         # авторизуем
#         session.add(Users(telegram_id=message.from_user.id, name=data["name"], surname=data["surname"], is_authenticated=True))
#         session.commit()
#     await message.answer("Авторизация прошла успешно!")
#     await state.clear()
    