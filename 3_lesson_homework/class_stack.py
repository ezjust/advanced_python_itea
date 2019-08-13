class Stack:
    def __init__(self):
        self.things = []

    def is_empty(self):
        return self.things == []

    def add(self, data):
        self.things.append(data)

    def remove(self, data):
        if data in self.things:
            self.things.remove(data)
            return f'Thing {data} has been deleted'

    def print_all(self):
        for item in self.things:
            print(item)
        return "That's it"


# Stack demo
s = Stack()

for i in range(10):
    s.add(f'new_thing_{i}')

print(s.print_all())





