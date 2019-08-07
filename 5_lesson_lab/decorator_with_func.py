from threading import Thread
import time


def decorator(name, is_daemon: bool=False):
    def inner(func):
        thread = Thread(target=func, args=(5, f'{name}'))
        if is_daemon is False:
            print(f'thread {name} starting')
            thread.start()
        if is_daemon is True:
            print(f'thread {name} starting as daemon')
            thread.daemon
        return func
    return inner  # this is the fun_obj mentioned in the above content


@decorator('new_thread', False)
def func(iterations, name):
    for i in range(iterations):
        print(f'the test number {i} is running')
        time.sleep(2)
    print('the test has been finished')



