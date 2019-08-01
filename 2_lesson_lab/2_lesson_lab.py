class Animal:
    def __init__(self, name, an_type):
      self.name = name
      self.an_type = an_type

    def __del__(self):
        print(f'')

    def eat(self):
        print("I'm eating")

    def move(self):
        print("I'm moving")

    def who_am_i(self):
        print(f'Name: {self.name}\nType: {self.an_type}')


new_animal = Animal('Human', 'Mammal')
new_animal.who_am_i()
