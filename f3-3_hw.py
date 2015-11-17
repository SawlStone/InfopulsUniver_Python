__author__ = 'Sawl_Stone'

class Car:
    def __init__(self, engine, tyre):
        self.engine = engine
        self.tyre = tyre



def main():
    C = Car(1.8, 4)
    print(C.engine, C.tyre)

main()