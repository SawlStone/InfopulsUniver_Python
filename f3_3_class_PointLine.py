__author__ = 'Sawl_Stone'

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    def distancePoints(self, otherPoint):
        math.sqrt((self.x-otherPoint.x)**2 + (self.y-otherPoint.y)**2)

class Line:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def distance(self):
        return self.begin.distancePoints(self.end)