class ComplexNumber:
    def __init__(self, x, y):
        self.complex_num = complex(x, y)

    def __add__(self, other):
        summation = self.complex_num.imag + other
        return summation

    def __sub__(self, other):
        subs = self.complex_num.imag - other
        return subs

    def __mul__(self, other):
        multiple = self.complex_num.imag * other
        return multiple

    def __truediv__(self, other):
        divide = self.complex_num.imag / other
        return divide


c = ComplexNumber(4, 5)
print(c.__add__(c.complex_num.real))
print(c.__sub__(c.complex_num.real))
print(c.__mul__(c.complex_num.real))
print(c.__truediv__(c.complex_num.real))
