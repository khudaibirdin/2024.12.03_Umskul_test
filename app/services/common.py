import inspect
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import asyncio


def get_function_name():
    current_function = inspect.currentframe().f_back.f_code.co_name
    return current_function


async def reset_state_after_timeout(state: FSMContext, time: int):
    """
    Функция сброса состояний
    """
    await asyncio.sleep(time)
    await state.clear()