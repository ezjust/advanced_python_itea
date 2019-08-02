from abc import ABC, abstractmethod
from datetime import datetime


class Person:

    def __init__(self, person):
        self._person = [person]

    @abstractmethod
    def show_info(self):
        return self._person

    @abstractmethod
    def get_age(self):
        age = int(datetime.now().strftime("%Y")) - int(self._person[1].split('.')[0])
        return age


class Pupil(Person):

    def __init__(self, surname, birth_date, faculty):
        self._person = (surname, birth_date, faculty)

    def show_info(self):
        return super().show_info()

    def get_age(self):
        return super().get_age()


class Student(Person):

    def __init__(self, surname, birth_date, faculty, level):
        self._person = (surname, birth_date, faculty, level)

    def show_info(self):
        return super().show_info()

    def get_age(self):
        return super().get_age()


class Teacher(Person):

    def __init__(self, surname, birth_date, faculty, position, job_stage):
        self._person = (surname, birth_date, faculty, position, job_stage)

    def show_info(self):
        return super().show_info()

    def get_age(self):
        return super().get_age()


a = Pupil('Vasylenko', '1990.30.03', 'electronics')
b = Student('Grygorenko', '1989.20.09', 'physics', '4')
c = Teacher('Chubenko', '1960.20.03', 'physics', 'professor', '25')
# print(a.get_age())
# print(b.show_info())
# print(b.get_age())
# print(c.get_age())
list_of_persons = []
list_of_persons.append(a)
list_of_persons.append(b)
list_of_persons.append(c)
for person in list_of_persons:
    print(person.show_info())
age = 40
for person in list_of_persons:
    if person.get_age() in range(age):
        print(f'Person {person.show_info()[0]} has needed age in range {age}, person age = {person.get_age()}')


