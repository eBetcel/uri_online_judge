"""In order to warm you up for this particular contest, we shall ask you to write a program which calculates the quotient and the remainder of the division of two integers, can that be? Recall that the quotient and the remainder of the division of an integer a by a non-zero integer b are respectively the only integers q and r such that 0 ≤ r < |b| and:

a = b × q + r

In case you don't know it, the theorem that guarantees the existence and the uniqueness of the integers q and r is known as ‘Euclidean Division Theorem’ or ‘Division Algorithm’.

Input
The input consists of two integers a and b (-1,000 ≤ a, b < 1,000).

Output
Print the quotient q followed by the remainder r of the division of a by b.

Input Samples	Output Samples
7 3

2 1

7 -3

-2 1

-7 3

-3 2"""

numbers = input().split()
a, b = numbers
a = float(a)
b = float(b)

q = a // b
r = a % b

if(r <0):
    r = -r 
q = int(q)
r = int(r)

print(q,  r)