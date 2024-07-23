from fastapi import FastAPI, Request

import os
from dotenv import load_dotenv
import requests

from utils import random_number, kospi, openai, langchain

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
URL = f'https://api.telegram.org/bot{TOKEN}'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app = FastAPI()


@app.post('/')
async def read_root(request: Request):
    body = await request.json()
    
    user_id = body['message']['from']['id']
    user_input = body['message']['text']

    if user_input[0] == '/':
        #우리가 만든 기능 추가
        if user_input == '/lotto':
            text = random_number()
        elif user_input == '/kospi':
            text = kospi()
        else:
            text = '지원하지 않는 기능입니다'
    else:
        #openAI API 활용
        #text = openai(OPENAI_API_KEY, user_input)
        text = langchain(OPENAI_API_KEY, user_input)

    req_url = f'{URL}/sendMessage?chat_id={user_id}&text={text}'
    requests.get(req_url)

    return {'Hello': 'World'}