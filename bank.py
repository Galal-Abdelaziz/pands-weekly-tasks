# bank.py
# Weekly Tasks 02
# This program is to sum two amounts(in Cents) entered by the user, and print out the result in Euros.
# author: Galal Abdelaziz
'''
This is the code with no error handling
x = input("Enter amount1(in cent): ")         # Asking user to enter first amount (variable).
y = input("Enter amount2(in cent): ")         # Asking user to enter second amount (variable)
number = int(x) + int(y)                      # Addeing both amounts as int.
answer = number /100                          # Dividing the total by 100 to get the amount in Euros.
print (f"The sum of these is €{answer}")      # used "f" to print text and answer.
'''

while True: # Start a while loop.
    try:    # try/except block to handle potential errors.
        x = input("Enter amount1(in cent): ")         # Ask the user to enter the first amount in cents (Str).
        if not x.isdigit() or int(x) < 0:             # Check if the input consists only of digits and is non-negative.
            raise ValueError("Please enter a whole number.")  # If not, raise a ValueError with a custom error message
        
        y = input("Enter amount2(in cent): ")         # Ask the user to enter the second amount in cents (Str).
        if not y.isdigit() or int(y) < 0:             # Check if the input consists only of digits and is non-negative.
            raise ValueError("Please enter a whole number.")  # If not, raise a ValueError with a custom error message.
        
        number = int(x) + int(y)                      # Convert the amounts to int and add them together.
        answer = number /100                          # Divide the total by 100 to get the amount in Euros (result in float).
        print (f"The sum of these is €{answer}")      # Print the answer with a formatted string.
        break                                         # Exit the loop if no errors occur.
    except ValueError as e:              # This error is raised when input is non-digits or negative.
        print(e)                         # Print the error message.
    except Exception as e:               # This error is raised when an unexpected exception occurs.
        print(f"An error occurred: {e}") # Print the error message.