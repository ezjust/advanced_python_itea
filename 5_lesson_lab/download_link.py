import urllib.request
from threading import Thread
import time

links_list = ['http://www.ovh.net/files/1Mb.dat',
              'http://www.ovh.net/files/10Mb.dat',
              'http://mirror.filearena.net/pub/speed/SpeedTest_16MB.dat',
              'http://mirror.filearena.net/pub/speed/SpeedTest_32MB.dat',
              'http://mirror.filearena.net/pub/speed/SpeedTest_64MB.dat']


path_to_links = '/Users/ezjust/advanced_python_itea/5_lesson_lab/links/'


def my_links_decorator(links: list):

    def inner(custom_function):

        count = 0
        for link in links:
            thread = Thread(target=custom_function, args=(link, 0), name=f'thread_{count}')
            thread.start()
            print(f'file started to be downloaded from link {link}')
            while thread.is_alive():
                print('file download is in progress')
                time.sleep(2)
            print(f"file {(link.split('/')[-1])} has been downloaded as link_{count}")
            count += 1
        return 'decorator ended'
    return inner


@my_links_decorator(links_list)
def download_link(link, count):
        urllib.request.urlretrieve(link, f'{path_to_links}link_{count}')







