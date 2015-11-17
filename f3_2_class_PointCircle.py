__author__ = 'Sawl_Stone'

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

class Circle:
    def __init__(self, p, radius):
        self.center = p
        self.radius = radius

    def square(self):
        return math.pi*self.radius*self.radius


def main():
    p = Point(3, 7)
    dis = p.distance()
    c = Circle(p, 10)
    sq = c.square()
    print(sq)

main()
