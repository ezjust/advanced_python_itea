from mongoengine import *
connect('lesson_9')  # connection to db


class User(Document):
    login = StringField(max_length=30)
    password = StringField(min_length=8)
    email = EmailField()
    role = StringField()


class Category(Document):
    title = StringField(max_length=30)
    description = StringField(max_length=1024)


class Item(Document):

    added_by = ReferenceField(User)
    category = ReferenceField(Category)
    is_available = BooleanField(default=True)
    name = StringField(required=True, max_length=255)
    description = StringField(max_length=2048, required=False)
    weight = FloatField(required=False)
#
#
# user_obj = User(login='EZ', password='12345678', email='3spirit3@ukr.net', role='admin')
# user = user_obj.save()
#
#
# category = {'title': 'LPD_team', 'description': 'LPD team is the best in Ring'}
# category_object = Category(**category)
# cat = category_object.save()
#
# item = {'added_by': user, 'category': cat, 'is_available': True, 'name': 'Pro1'}
# item_obj = Item(**item)
# it = item_obj.save()


items = Item.objects()
for i in items:
    print(i.id)

