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

class Parellologram(Quadrangle):
    def __init__(self, line1, line2, angle):
        Quadrangle.__init__(self, line1, line2, line1, angle, 180-angle)

class Rectangle(Parellologram):
    def __init__(self, line1, line2):
        Parellologram.__init__(self, line1, line2, 90)

class Rombus(Parellologram):
    def __init__(self, line, angle):
        Parellologram.__init__(self, line, line, angle)



def main():
    par = Parellologram(10, 20, 15)
