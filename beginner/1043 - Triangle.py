"""
Read three point floating values (A, B and C) and verify if is possible to make a triangle with them. If it is possible, calculate the perimeter of the triangle and print the message:


Perimetro = XX.X


If it is not possible, calculate the area of the trapezium which basis A and B and C as height, and print the message:


Area = XX.X

Input
The input file has tree floating point numbers.

Output
Print the result with one digit after the decimal point.

Input Sample	Output Sample
6.0 4.0 2.0

Area = 10.0

6.0 4.0 2.1

Perimetro = 12.1
"""
def validate_triangle(a, b, c):
    if((a + b > c) and (a + c > b) and (b + c > a)):
        return True
    else:
        return False

sides = input().split()
a, b, c = sides

a = float(a)
b = float(b)
c = float(c)

if(validate_triangle(a, b,c)):
    perimeter = a + b + c
    print("Perimetro = {:.1f}".format(perimeter))

else:
    area = ((a + b) * c) / 2
    print("Area = {:.1f}".format(area))