class Stack:
    def __init__(self):
        self.things = []

    def is_empty(self):
        return self.things == []

    def add(self, data):
        self.things.append(data)
        return f'New thing {data} is added'

    def remove(self, data):
        if data in self.things:
            self.things.remove(data)
            return f'Thing {data} has been deleted'

    def print_all(self):
        for item in self.things:
            print(item)
        return "That's it"


s = Stack()
print(s.is_empty())
print(s.add('first_thing'))
print(s.is_empty())
print(s.add('second_thing'))
print(s.add('third_thing'))
print(s.remove('second_thing'))
print(s.print_all())
