# bank.py
# Weekly Tasks 02
# This program is to sum two amounts(in Cents) entered by the user, and print out the result in Euros.
# author: Galal Abdelaziz

x = input("Enter amount1(in cent): ")
y = input("Enter amount2(in cent): ")
number = int(x) + int(y)
answer = number /100
print (f"The sum of these is €{answer}")