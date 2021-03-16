"""Read three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

Input
The input contains three integer numbers.

Output
Present the output as requested above.
"""

array = input().split()

a, b, c = array

a_list = [int(a), int(b), int(c)]

sorted_list = sorted(a_list)

for n in sorted_list:
    print(n)

print("")

for n in a_list:
    print(n)