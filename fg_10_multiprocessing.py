__author__ = 'Sawl_Stone'

# multiprocessing

from multiprocessing import Process, Queue
import time

def sum(queue, begin, end):
    result = 0
    for i in range(begin, end):
        result += i

    queue.put(result)

def main():
    if __name__ == '__main__':
        queue = Queue()
        p1 = Process(target=sum, args=(queue, 0, 2500000))
        p2 = Process(target=sum, args=(queue, 2500000, 5000000))
        p3 = Process(target=sum, args=(queue, 5000000, 7500000))
        p4 = Process(target=sum, args=(queue, 7500000, 10000001))

        now_1 = time.time()
        p1.start()
        now_2 = time.time()

        now_3 = time.time()
        p2.start()
        now_4 = time.time()

        now_5 = time.time()
        p3.start()
        now_6 = time.time()

        now_7 = time.time()
        p4.start()
        now_8 = time.time()

        p1.join()
        p2.join()
        p3.join()
        p4.join()

        total_result = queue.get() + queue.get()
        print(total_result)
        print(now_2 - now_1)
        print(now_4 - now_3)
        print(now_6 - now_5)
        print(now_8 - now_7)

main()