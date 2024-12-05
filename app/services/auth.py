from internal.database import get_session
from app.models.common import Users


def is_registered(telegram_id:str) -> bool:
    """
        Проверка зарегистрирован ли пользователь
    """
    with get_session() as session:
        user = session.query(Users).filter(Users.telegram_id == telegram_id).first()
    if not user:
        return False
    else:
        return True