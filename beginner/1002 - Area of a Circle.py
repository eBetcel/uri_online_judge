class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def calc_area(self):
        return self.__radius ** 2 * 3.14159

r = float(input())

circle = Circle(r)
a = circle.calc_area()
print("A=%.4f" %a)