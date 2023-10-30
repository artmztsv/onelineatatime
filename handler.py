import sys
import os

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import telegram
import random

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = <-1002036026113>

def send_photo(event, context):
    bot = telegram.Bot(token=TOKEN)
    photo_url = 'flashcards_folder/'
    rand_photo = random.choice(os.listdir(photo_url))
    with open(os.path.join(photo_url, rand_photo), 'rb') as file:
        bot.sendPhoto(chat_id = -1002036026113, photo = file)
