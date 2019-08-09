from threading import Thread
import time


def my_decorator(name, is_daemon: bool=False):

    def inner(custom_function):

        thread = Thread(target=custom_function, name=f'{name}')
        if is_daemon is False:
            thread.start()
            print(f'thread {name} started')
        elif is_daemon is True:
            thread.daemon
            print(f'thread {name} started as daemon')
        while thread.is_alive():
            print(f'thread {name} is still running')
            time.sleep(1)
        else:
            print(f'thread {name} has been finished')
        return custom_function
    return inner  # this is the fun_obj mentioned in the above content


@my_decorator('new_thread', False)
def func():
    time.sleep(2)




