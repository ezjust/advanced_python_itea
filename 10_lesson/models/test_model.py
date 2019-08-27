from mongoengine import *

connect('lesson_10_rest')


class Category(Document):
    name = StringField()

    @property
    def items(self):
        return Item.objects(category=self)


class Item(Document):
    name = StringField()
    description = StringField()
    category = ReferenceField(Category)


