import telebot
import requests
from bs4 import BeautifulSoup
import datetime


bs = BeautifulSoup(requests.get('https://www.cifrus.ru/catalog/smartfony/google/pixel-7-pro').text, 'html')
captions = bs.find_all('div', class_='caption')
text = [['❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗', f'Цены на момент {datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year}']]
for i in captions:
    name = i.find('div', class_='name')
    div = i.find('div', class_='price')
    price_new = div.find('span', class_='price-new')
    text.append([name.text, price_new.text])


token = "5250850691:AAEw3FPVeDo8u59NvpNV0r5zijgsHEUw2AM"
bot = telebot.TeleBot(token)
bot.send_message('449567677', '\n\n'.join('\n'.join(i) for i in text))