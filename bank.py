# bank.py
# Weekly Tasks 02
# This program is to sum two amounts(in Cents) entered by the user, and print out the result in Euros.
# author: Galal Abdelaziz

x = input("Enter amount1(in cent): ")
y = input("Enter amount2(in cent): ")
number = int(x) + int(y)                      # Added both amounts as int.
answer = number /100                          # Divided the total by 100 to get the amount in Euros.
print (f"The sum of these is €{answer}")      # used "f" to print text and answer/int.