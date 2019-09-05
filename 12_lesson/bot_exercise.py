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
def username_handler(message):
    if message.text != 'start' and message.text != '':
        user_data['username'] = message.text
        bot.send_message(message.chat.id, '-------------\nEmail:\n------------')
        write_to_shelve('state', 1)


@bot.message_handler(func=lambda m: read_from_shelve('state') == 1)
def email_handler(message):
    if message.text != '':
        user_data['email'] = message.text
        bot.send_message(message.chat.id, '------------\nPhone:\n------------')
        write_to_shelve('state', 2)


@bot.message_handler(func=lambda m: read_from_shelve('state') == 2)
def phone_handler(message):
    if message.text != '':
        user_data['phone'] = message.text
        bot.send_message(message.chat.id, '------------\nAddress:\n------------')
        write_to_shelve('state', 3)


@bot.message_handler(func=lambda m: read_from_shelve('state') == 3)
def address_handler(message):
    user_data['address'] = message.text
    bot.send_message(message.chat.id, '-------------\nWishes:\n-------------')
    write_to_shelve('state', 4)


@bot.message_handler(func=lambda m: read_from_shelve('state') == 4)
def comment_handler(message):
    user_data['wishes'] = message.text
    bot.send_message(message.chat.id, 'Hooray!!!User successfully saved')
    print(user_data)
    new_user = User(username=user_data['username'], email=user_data['email'], phone=user_data['phone'], address=user_data['address'], wishes=user_data['wishes'])
    new_user.save()


if __name__ == '__main__':
    print('Bot started')
    bot.polling()
