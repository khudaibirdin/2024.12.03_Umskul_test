import asyncio
from dotenv import load_dotenv
from aiogram import Dispatcher

import app.routes.auth.register
import app.routes.business.enter_scores
import app.routes.business.view_scores
import app.routes.common
import app.routes.business
import app.routes.auth

from app.bot import bot
import app.routes.common
from internal.database import init_db

load_dotenv()

dp = Dispatcher()

init_db()

async def main():
    dp.include_routers(app.routes.common.router)
    dp.include_routers(app.routes.auth.register.router)
    dp.include_routers(app.routes.business.enter_scores.router)
    dp.include_routers(app.routes.business.view_scores.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())