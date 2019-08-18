class Test:

    __slots__ = "_a", "_b"

    my_list = [1, 2, 3]

    b = my_list.__iter__()

    a = iter(my_list)

    print(next(b))


a = Test








