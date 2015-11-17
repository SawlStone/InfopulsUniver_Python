__author__ = 'Sawl_Stone'

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

#class Circle:
#    def __init__(self, p, radius):
#        self.centr = p
#        self.radius = radius

class Circle1(Point):
    def __init__(self, p, radius):
        Point.__init__(self, p.x, p.y)
        self.radius = radius

def distanceBetweenPoints(p1, p2):
    return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)


def main():
    p1 = Point(3, 4)
    p2 = Point(5, 6)
    result = distanceBetweenPoints(p1, p2)
    print(result)
main()