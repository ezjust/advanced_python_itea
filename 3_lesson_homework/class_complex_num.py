class ComplexNumber:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        if self._y < 0:
            return f"{self._x}-{abs(self._y)}*i"
        return f"{self._x}+{self._y}*i"

    def __add__(self, other):
        real = self._x + other.x
        imag = self._y + other.y
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self._x - other._x
        imag = self._y - other._y
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self._x * other._x - self._y * other._y
        imag = self._x * other._y + other._x * self._y
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        real = self._x * other._x + self._y * other._y
        imag = self._y * other._x - self._x * other._y
        divider = float(other._x ** 2 + other._y ** 2)
        return ComplexNumber(real / divider, imag / divider)


c = ComplexNumber(4, 5)
c1 = ComplexNumber(-3, 5)
print(c)
print(c1)
result = c * c1
print(result)
result_1 = c / c1
print(result_1)
