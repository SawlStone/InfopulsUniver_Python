__author__ = 'Sawl_Stone'

class Quadrangle:
    def __init__(self, line1, line2, line3, angle1, angle2):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.angle1 = angle1
        self.angle2 = angle2

    def square(self):
        return 100

class Parallologram(Quadrangle):
    def __init__(self, line1, line2, angle):
        Quadrangle.__init__(self, line1, line2, line1, angle, 180-angle)

class Rectangle(Parallologram):
    def __init__(self, line1, line2):
        Parallologram.__init__(self, line1, line2, 90)

class Rombus(Parallologram):
    def __init__(self, line, angle):
        Parallologram.__init__(self, line, line, angle)

class Square(Rectangle, Rombus):
    def __init__(self, line):
        Rectangle.__init__(self, line, line)
        Rombus.__init__(self, line, 90)

def main():
    s = Square(10)
    print(s.__dict__)

main()