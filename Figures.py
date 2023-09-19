from math import pi


class Figure:

    def area(self):
        pass

    def exist(self):
        pass

    def perimeter(self):
        pass


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.exist():
            raise ValueError("triangle doesn't exist")

    def exist(self):
        if self.a > 0 and self.b > 0 and self.c > 0:
            if ((self.a + self.b) > self.c and
                    (self.b + self.c) > self.a and
                    (self.c + self.a) > self.b):
                return True
        return False

    def perimeter(self):
        return float(self.a + self.b + self.c)

    def area(self):
        p = self.perimeter() / 2.0
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**(1/2)

    def is_rectangular(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return True
        return False


class Circle(Figure):

    def __init__(self, r):
        self.r = r
        if not self.exist():
            raise ValueError("circle doesn't exist")

    def exist(self):
        if self.r > 0:
            return True
        return False

    def area(self):
        return pi * self.r ** 2


if __name__ == '__main__':
    cr = Circle(10)
    print(cr.area())
    tr = Triangle(3, 5, 4)
    print(tr.area())
    print(tr.is_rectangular())
