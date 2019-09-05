from mongoengine import *
from . constants import salary_choices

connect('employees')


class Role(EmbeddedDocument):
    name = StringField()
    grade = StringField()
    experience = IntField(min_value=1)


class Salary(Document):
    type = StringField(choices=salary_choices)
    amount = IntField(min_value=3200)
    fees = IntField(required=True)
    comment = StringField(max_length=2048)

    @property
    def net_salary(self):
        return self.amount - self.fees

    @property
    def commentary(self):
        return self.comment

    @comment.setter
    def commentary(self, value):
        if isinstance(value, str):
            self.comment = value
            return self.comment
        raise TypeError('Wrong type')


class Employee(Document):
    name = StringField(max_length=255)
    surname = StringField(max_length=255)
    email = EmailField()
    role = EmbeddedDocumentField(Role)
    salary_payments = ListField(ReferenceField(Salary))



