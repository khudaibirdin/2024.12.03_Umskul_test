import os
from aiogram import Bot


api_token = os.getenv('TG_API_TOKEN')
bot = Bot(token=api_token)