class Test:

    def __init__(self, x):
        self._x = x

    def set_x(self, x):
        self._x = x
        print('setter')

    def get_x(self):
        return self._x
        print('getter')
    def del_x(self):
        del self._x
        print('deleter')
    x = property(get_x, set_x, del_x)


obj = Test(100)
obj.x
obj.x = 'new_value'
del obj.x


