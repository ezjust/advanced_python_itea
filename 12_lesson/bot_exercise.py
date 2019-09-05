import telebot
import shelve
from mongoengine import *
from mongo_base import User
connect('telegram_info')

TOKEN = '820284949:AAGs-x6UPt-LWV8mMsS8Xl0WH1sYzomx7GE'

bot = telebot.TeleBot(TOKEN)
user_data = {}


def write_to_shelve(key, value):
    with shelve.open('test_shelf.db') as s:
        s[key] = value


def read_from_shelve(key):
    with shelve.open('test_shelf.db') as s:
        return s[key]


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Hello, this is telegram bot that collect data about user'
                                      '\n\n------------\nNew User:\n------------')
    write_to_shelve('state', 0)


@bot.message_handler(func=lambda m: read_from_shelve('state') == 0)
def username(message):
    if message.text != 'start' and message.text != '':
        user_data['username'] = message.text
        write_to_shelve('state', 1)


@bot.message_handler(func=lambda m: read_from_shelve('state') == 1)
def insert_email(message):
    bot.send_message(message.chat.id, '-------------\nEmail:\n------------')
    if message.text != '':
        user_data['email'] = message.text
        write_to_shelve('state', 2)


@bot.message_handler(func=lambda m: read_from_shelve('state') == 2)
def insert_phone(message):
    bot.send_message(message.chat.id, '------------\nPhone:\n------------')
    if message.text != '':
        user_data['phone'] = message.text
        write_to_shelve('state', 3)


@bot.message_handler(func=lambda m: read_from_shelve('state') == 3)
def insert_address(message):
    bot.send_message(message.chat.id, '------------\nAddress:\n------------')
    user_data['address'] = message.text
    write_to_shelve('state', 4)


@bot.message_handler(func=lambda m: read_from_shelve('state') == 4)
def insert_comment(message):
    bot.send_message(message.chat.id, '-------------\nWishes:\n-------------')
    user_data['wishes'] = message.text
    write_to_shelve('state', 5)
    print(user_data)
    new_user = User(username=user_data['username'], email=user_data['email'], phone=user_data['phone'], address=user_data['address'], wishes=user_data['wishes'])
    new_user.save()


@bot.message_handler(func=lambda m: read_from_shelve('state') == 5)
def insert_comment(message):
    bot.send_message(message.chat.id, 'Hooray!!!User successfully saved')


if __name__ == '__main__':
    print('Bot started')
    bot.polling()
