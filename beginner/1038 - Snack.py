"""Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.



Input
The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point."""

order = input().split()

code, quantity = order
quantity = float(quantity)

menu = {   
    "1": 4.00,
    "2": 4.50,
    "3": 5.00,
    "4": 2.00,
    "5": 1.50
}

total = menu[code] * quantity
print("Total: R$ {:.2f}".format(total))