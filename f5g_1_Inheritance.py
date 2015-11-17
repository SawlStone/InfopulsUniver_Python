__author__ = 'Sawl_Stone'

class A:
    def __init__(self):
        print("A")

    def f(self):
        print("f")

class B:
    def __init__(self):
        A.__init__(self)
        print("B")

class C(A):
    def __init__(self):
        A.__init__(self)
        print("C")

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("D")


def main():
    d = D()
    d.f()

main()