#Taking four inputs at a time
a, b, c, d = input().split()

#Casting splitted string to integers
a = int(a)
b = int(b)
c = int(c)
d = int(d)

#Condition
if(b > c and  d > a and ((c + d) > (a + b)) and (c >= 0 and d >= 0) and (a % 2 == 0)):
    print("Valores nao aceitos") 
else:
    print("Valores aceitos")