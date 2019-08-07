from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler
import random
import time


def random_generator(num, thread_name):
    for i in range(num):
        time.sleep(random.randint(0, 5))
        print(f"I'm executing in {thread_name}")
    print(f'{thread_name} has been closed')


thread_1 = Thread(target=random_generator, args=(5, 'thread_1'))
thread_2 = Thread(target=random_generator, args=(5, 'thread_2'))

thread_1.start()
thread_2.start()
# thread_1.join()
# thread_2.join()


# def write_to_file(filename, num_of_lines):
#     with open(filename, 'w') as f:
#         for i in range(num_of_lines):
#             f.write(str(random.randint(0, 500)))
#
#
# list_of_threads = []
# for i in range(10):
#     t = Thread(target=write_to_file, args=(f'{random.randint(0, 1000)}.txt', random.randint(0, 100)))
#     list_of_threads.append(t)
#     t.start()

# class RandomGeneratorThread(Thread):
#
#     def __init__(self, num, name):
#         self._num = num
#         self._name = name
#         Thread.__init__(self, name=self._name)
#
#     def run(self):
#         for i in range(self._num):
#             time.sleep(random.randint(0, 5))
#             print(f"I'm executing in {self._name}")
#         print(f'{self._name} has been closed')
#
#
# a = RandomGeneratorThread(10, 'Thread a')
# b = RandomGeneratorThread(10, 'Thread b')
# # a.start()
# # b.start()
#
# def some_job():
#     print('10 seconds gone')
#
# sched = BackgroundScheduler()
# sched.add_job(some_job, 'interval', seconds=1)
# sched.start()
#
# while True:
#     pass