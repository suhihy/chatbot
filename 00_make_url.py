import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

URL = 'https://api.telegram.org/bot'

print(f'{URL}{TOKEN}/getMe')