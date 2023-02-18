import telebot
import requests
from bs4 import BeautifulSoup
import os


token = "5250850691:AAEw3FPVeDo8u59NvpNV0r5zijgsHEUw2AM"
bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def start(message: telebot.types.Message):
#     print(message.chat.id)
#     bot.send_message(message.chat.id, f'Привет! {message.from_user.full_name}')


def send_message():
    req = requests.get('https://www.cifrus.ru/catalog/smartfony/google')
    bs = BeautifulSoup(req.text, 'html')
    name = bs.find_all('div', class_='name')[3]
    price = bs.findAll('span', class_='price-new')[3]
    data = []
    with open('file.txt', 'r+') as f:
        for i in f.readlines():
            data.append(i)
    if data[0][0:-1] != name.text:
        bot.send_message(449567677, 'Товар изменился')
    elif data[1] != price.text:
        bot.send_message(449567677, f'{name.text}\n\n{price.text}')
        with open('file.txt', 'w') as f:
            f.write(name.text+'\n')
            f.write(price.text)


send_message()