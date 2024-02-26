# collatz.py
# Weekly Tasks 04
# This program asks the user to input any positive integer and outputs the successive values of the Collatz conjecture.
# author: Galal Abdelaziz.

x = int(input("Please enter a positive number:"))     # Asking user to enter a number (variable).

while x != 1:                                         # using a while loop to get the results.
    
    if x < 1:                                         # using this line to avoid infint loop in the case of negative numbers.
        print("You can only use a positive number")   # user will get this error if entered negative numbers.
        break                                         # Stops the loop, to avoid an infinite loop.
        
    elif x % 2 == 0:                                  # Testing for even numbers.
            x = (x // 2)                              # Dividing by 2
            
    elif x % 2 == 1:                                  # Testing for odd numbers.
            x = (3 * x + 1)                           # Multiplying by 3 then adding 1.
            
    print(x, end=" ")                                 # Printing results, used (end=" ") to have all results on the same line separated by a space.