import time


def decorator(repeats):
    start = time.time()

    def func_decorator(func):
        def wrapper():
            for i in range(repeats):
                end = time.time()
                spent_time = end - start
                func()
            return spent_time, func.__name__
        return wrapper
    return func_decorator


@decorator(10)
def say_hello():
    print('Hellllooooo')


print(say_hello())
