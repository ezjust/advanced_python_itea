from mongoengine import *
connect('telegram_info')


class User(Document):
    username = StringField(max_length=50, required=True)
    email = EmailField(min_length=7, required=True)
    phone = StringField(min_length=10, required=True)
    address = StringField(max_length=50)
    wishes = StringField(max_length=100)


user_data = {'username': 'Ez Pizzy', 'email': 'ez@ukr.net', 'phone': '0501761602', 'address': 'volynska street', 'wishes': ' '}
new_user = User(username=user_data['username'], email=user_data['email'], phone=user_data['phone'], address=user_data['address'], wishes=user_data['wishes'])
new_user.save()
