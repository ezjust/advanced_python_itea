from mongoengine import *
connect('telegram_info')


class User(Document):
    username = StringField(max_length=50, required=True)
    email = EmailField(min_length=7, required=True)
    phone = StringField(min_length=10, required=True)
    address = StringField(max_length=50)
    wishes = StringField(max_length=100)
