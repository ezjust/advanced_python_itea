class Dots:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z

    def __add__(self, other):
        x, y, z = self.get_x() + other.get_x(), self.get_y() + other.get_y(), self.get_z() + other.get_z()
        return Dots(x, y, z)

    def __sub__(self, other):
        x, y, z = self.get_x() - other.get_x(), self.get_y() - other.get_y(), self.get_z() - other.get_z()
        return Dots(x, y, z)

    def __mul__(self, other):
        x, y, z = self.get_x() * other.get_x(), self.get_y() * other.get_y(), self.get_z() * other.get_z()
        return Dots(x, y, z)

    def __truediv__(self, other):
        x, y, z = self.get_x() / other.get_x(), self.get_y() / other.get_y(), self.get_z() / other.get_z()
        return Dots(x, y, z)

    def __repr__(self):
        return f'x = {self._x}, y = {self._y}, z = {self._z}'


p1 = Dots(1, 2, 3)
p2 = Dots(1, 2, 3)

print(p1 * p2)


