"""
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.

Input Samples	Output Samples
10.0 20.1 5.1

R1 = -0.29788
R2 = -1.71212

0.0 20.0 5.0

Impossivel calcular

10.3 203.0 5.0

R1 = -0.02466
R2 = -19.68408

10.0 3.0 5.0

Impossivel calcular
"""
import math

numbers = input().split()

a, b, c = numbers

a = float(a)
b = float(b)
c = float(c)

delta = b * b - 4 * a * c

if(delta < 0 or a == 0):
    print('Impossivel calcular')

else:
    r1 = (-b + math.sqrt(delta)) / (2 * a) 
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))