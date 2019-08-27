from mongoengine import *
connect('Students_base')


class Student(Document):
    full_name = StringField(max_length=50)
    group = IntField(max_length=2)
    marks = EmbeddedDocument(DictField())
    mentor = StringField(max_length=50)
    faculty = StringField(max_length=30)


student_1 = Student(full_name='Ez Ezevych Zucker', group=1, marks={'mathematics': 5, 'physics': 4}, mentor='Valeriy Utkin', faculty='Electronics')
student_2 = Student(full_name='Ez Ezevych Zucker', group=1, marks={'mathematics': 4, 'physics': 5}, mentor='Valeriy Suitkin', faculty='Physics')
save_new_student = student_1.save()
save_new_student_2 = student_2.save()




