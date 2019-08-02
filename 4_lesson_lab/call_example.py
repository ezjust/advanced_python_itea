class A:

    def __init__(self, var):
        self._var = 10

    def __call__(self, *args, **kwargs):
        return self._var


a = A(10)()
print(a)
