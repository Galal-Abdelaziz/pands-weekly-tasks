# accounts.py
# Weekly Tasks 03
# This program reads a 10 digits account number and outputs the account number with only the last 4 digits showing.
# author: Galal Abdelaziz
'''
This is the basic code to read and mask any lenght account number with no error handling
answer = input("Please enter an 10 digit account number:")  # Asking user to enter an account number (variable).
print ("x" * (len(answer) - 4) + answer[-4:]) # used len and -4 to replace all of the numbers with x's ("x"* int = "x") other than last 4 digits, Used answer[-4:] to show only the last 4 digits.
'''

while True:  # Start a while loop.
    try:  # try/except block to handle potential errors.
        answer = input("Please enter an 10 digit account number:") # Ask the user to enter an account number
        
        if not answer.isdigit():  # Check if the input is a number
            raise ValueError("Account number must only contain digits.")
            
        if len(answer)!= 10: # Check if the input is 10 digits long
            raise ValueError("Account number must be exactly 10 digits long.")
            
        print ("x" * (len(answer) - 4) + answer[-4:]) # Print the masked account number with 'x' as masking character
        
        break # Exit the loop if the input is valid

    except ValueError as e: # Catch the ValueError exception
        print(e) # Print the error message and continue the loop