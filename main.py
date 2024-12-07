import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse

load_dotenv()
TG_TOKEN = os.getenv('TELEGRAM_TOKEN')
TG_CHAT_ID = '718815563'
bot = ptbot.Bot(TG_TOKEN)


def reply(chat_id, text):
    time_sec = parse(text)
    message_id = bot.send_message(chat_id, f"Осталось {time_sec} секунд \n"
                                           f"{render_progressbar(time_sec, 0)}")
    bot.create_countdown(time_sec, notify, author_id=chat_id, message_id=message_id, total_time=time_sec)


def notify(sec_left, author_id, message_id, total_time):
    current_sec = total_time - sec_left
    if sec_left > 0:
        bot.update_message(author_id, message_id, f"Осталось {sec_left} секунд!\n"
                                                  f"{render_progressbar(total_time, current_sec)}")
    else:
        bot.update_message(author_id, message_id, f"Осталось {sec_left} секунд!\n"
                                                  f"{render_progressbar(total_time,current_sec)}")
        bot.send_message(author_id,  "Время вышло!")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    bot.reply_on_message(reply)
    bot.run_bot()


if __name__ == '__main__':
    main()