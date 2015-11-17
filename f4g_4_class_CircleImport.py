__author__ = 'Sawl_Stone'

import f4g_3_class_PointCircle2
import math
class Circle(f4g_3_class_PointCircle2.Point):
    def __init__(self, x, y, radius):
        f4g_3_class_PointCircle2.Point.__init__(self, x, y)
        self.radius = radius

    def square(self):
        return math.pi*self.radius*self.radius

def main():
    c1 = Circle(3, 4, 10)
    c2 = Circle(5, 6, 20)
