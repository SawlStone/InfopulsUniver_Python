__author__ = 'Sawl_Stone'

# mnogopotochnost

import threading
import queue

class Producer(threading.Thread):
    def __init__(self, queue, mutex, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire() # zaxwat flaga(mutex)
            while self.queue.qsize() >= 10: #prowerka mesta w tumbochke
                self.mutex.wait()

            self.queue.put(1)
            self.mutex.notifyAll()
            self.mutex.release() # oswobogdaem mutex
            print("Thread " + self.name + " put the element into the queue")

class Consumer(threading.Thread):
    def __init__(self, queue, mutex, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire()
            while self.queue.qsize() == 0:
                self.mutex.wait()

            element = self.queue.get()
            self.mutex.notifyAll()
            self.mutex.release()
            print("Thread " + self.name + " get the element " + str(element) + " from queue")

def main():
    q = queue.Queue()
    mutex = threading.Condition()
    p1 = Producer(q, mutex, "p1")
    p2 = Producer(q, mutex, "p2")
    p3 = Producer(q, mutex, "p3")

    c1 = Consumer(q, mutex, "c1")
    c2 = Consumer(q, mutex, "c2")
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    c1.join()
    c2.join()

main()