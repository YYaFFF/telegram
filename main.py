import os
import ptbot
from dotenv import load_dotenv
import random
from pytimeparse import parse

load_dotenv()
TG_TOKEN = os.getenv('TELEGRAM_TOKEN')
TG_CHAT_ID = '718815563'
bot = ptbot.Bot(TG_TOKEN)


def reply(chat_id,text):
    time_sec = parse(text)
    bot.create_countdown(time_sec, notify, author_id=chat_id)


def notify(secs_left, author_id):
    if secs_left > 0:
        message_id = bot.send_message(author_id, f"Осталось {secs_left} секунд!")
    elif secs_left == 0:
        bot.send_message(author_id, "Осталось 0 секунд")
        bot.send_message(author_id,"Время вышло!")

bot.reply_on_message(reply)
bot.run_bot()

