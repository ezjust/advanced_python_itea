class MyArray:
    __slots__ = "_size", "_my_type", "_array"

    def __init__(self, size, my_type):
        self._size = size
        self._my_type = my_type
        self._array = [0] * self._size

    def __getitem__(self, idx):
        if idx > self._size - 1:
            raise StopIteration('Out of range')
        return self._array[idx]

    def __setitem__(self, idx, value):
        if isinstance(value, self._my_type):
            self._array[idx] = value
        else:
            raise TypeError('Wrong type')

    def __len__(self, other):
        return len(self._array)


arr = MyArray(10, int)
arr[0] = 2

for i in arr:
    print(i)
