__author__ = 'Sawl_Stone'

import threading

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
    s1 = Sum(1, 5000)
    s2 = Sum(5000, 10001)
    s1.start() # 'start' - sozdaet potok i atomatom wyzywaet metod 'run'
    s2.start()
    s1.join() # zastalyaet potok 'main' ostanowitsya, poka wtoroj ne zawersit rabotu
    s2.join()
    res1 = s1.result
    res2 = s2.result
    res = res1 + res2
    print(res)

main()
