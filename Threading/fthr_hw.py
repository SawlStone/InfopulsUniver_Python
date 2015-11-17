__author__ = 'Sawl_Stone'

import threading
import time
class Sum(threading.Thread):
    def __init__(self, begin, end):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end
        self.result = 0

    def run(self):
        for i in range(self.begin, self.end):
            self.result += i

def main():
    s1 = Sum(1, 2500000)
    s2 = Sum(2500000, 5000000)
    s3 = Sum(5000000, 7500000)
    s4 = Sum(7500000, 10000001)

    now_1 = time.time()
    s1.start() # 'start' - sozdaet potok i atomatom wyzywaet metod 'run'
    now_2 = time.time()

    now_3 = time.time()
    s2.start()
    now_4 = time.time()

    now_5 = time.time()
    s3.start()
    now_6 = time.time()

    now_7 = time.time()
    s4.start()
    now_8 = time.time()

    s1.join() # zastalyaet potok 'main' ostanowitsya, poka wtoroj ne zawersit rabotu
    s2.join()
    s3.join()
    s4.join()
    res1 = s1.result
    res2 = s2.result
    res = res1 + res2
    print(res)
    print(now_2 - now_1)
    print(now_4 - now_3)
    print(now_6 - now_5)
    print(now_8 - now_7)

main()
