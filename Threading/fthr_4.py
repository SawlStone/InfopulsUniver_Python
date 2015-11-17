__author__ = 'Sawl_Stone'

# Violinists and Bows

import threading
import time
import queue

class Violinist(threading.Thread):
    def __init__(self, queueViolins, queueBows, mutexV, mutexB, name):
        threading.Thread.__init__(self)
        self.queueViolins = queueViolins
        self.queueBows = queueBows
        self.mutexV = mutexV
        self.mutexB = mutexB
        self.name = name

    def run(self):
        self.mutexV.acquire() #zahwat flaga

        while (self.queueViolins.qsize() == 0):
            self.mutexV.wait()

        violin = self.queueViolins.get()
        self.mutexV.release() #snali flag

        self.mutexB.acquire()

        while (self.queueBows.qsize() == 0):
            self.mutexB.wait()

        bow = self.queueBows.get()
        self.mutexB.release()
        print("Violinist" + self.name + " is playing")
        time.sleep(10)

        self.mutexB.acquire()
        self.queueBows.put(bow)
        self.mutexB.notifyAll() # uwidomlenie poyavleniya
        self.mutexB.release()

        self.mutexV.acquire()
        self.queueViolins.put(violin)
        self.mutexV.notifyAll()
        self.mutexV.release()

def main():
    queueV = queue.Queue()
    queueV.put("violin1")
    queueV.put("violin2")
    queueV.put("violin3")

    queueB = queue.Queue()
    queueB.put("bow1")
    queueB.put("bow2")

    mutexViolin = threading.Condition()
    mutexBow = threading.Condition()

    v1 = Violinist(queueV, queueB, mutexViolin, mutexBow, "v1")
    v2 = Violinist(queueV, queueB, mutexViolin, mutexBow, "v2")
    v3 = Violinist(queueV, queueB, mutexViolin, mutexBow, "v3")
    v4 = Violinist(queueV, queueB, mutexViolin, mutexBow, "v4")

    v1.start()
    v2.start()
    v3.start()
    v4.start()

    v1.join()
    v2.join()
    v3.join()
    v4.join()

main()