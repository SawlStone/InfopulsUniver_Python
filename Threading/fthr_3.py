__author__ = 'Sawl_Stone'

# dead lock

import threading
import time
class MyThread(threading.Thread):
    def __init__(self, mutex1, mutex2):
        threading.Thread.__init__(self)
        self.mutex1 = mutex1
        self.mutex2 = mutex2

    def run(self):
        self.mutex1.acquire()
        time.sleep(5)
        self.mutex2.acquire()
        print("Everything is ok")
        self.mutex2.release()
        self.mutex1.release()

def main():
    mutex_1 = threading.Condition() # 'Condition - eto flagok'
    mutex_2 = threading.Condition()

    t1 = MyThread(mutex_1, mutex_2)
    t2 = MyThread(mutex_2, mutex_1)

    t1.start()
    t2.start()

main()