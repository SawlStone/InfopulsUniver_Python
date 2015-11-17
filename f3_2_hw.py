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

class CircleSektor:
    def __init__(self, L, radius):
        self.circ_arc = L
        self.radius = radius

    def cirrc_arc_square(self):
        return self.circ_arc * self.radius / 2

def main():
    p = Point(3, 7)
    dis = p.distance()
    c = Circle(p, 10)
    sq = c.square()
    cs = CircleSektor(3, 7)
    sek_sq = cs.cirrc_arc_square()
    print(sek_sq)

main()