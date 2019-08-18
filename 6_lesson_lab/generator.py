class NumGenerator:

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            self._start += 1
            return self._start
        raise StopIteration("end of structure")


a = NumGenerator(0, 3)
for i in a.__next__():
    print(i)
