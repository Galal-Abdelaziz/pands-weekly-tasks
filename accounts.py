# accounts.py
# Weekly Tasks 03
# This program reads an account number in any length and outputs the account number with only the last 4 digits showing.
# author: Galal Abdelaziz

answer = input("Please enter an 10 digit account number:")  # Asking user to enter an account number (variable).

'''
# Can use lines 10-14 (to replace line 16) to restrict input to 10 digits restarts the script until user adds 10 digits using if condition statment.
if len(answer) != 10:
        print ("Please enter 10 digits")
if len(answer) == 10:

        print ("x" * (len(answer) - 4) + answer[-4:])
'''
print ("x" * (len(answer) - 4) + answer[-4:]) # used len and -4 to replace all of the numbers with x's ("x"* int = "x") other than last 4 digits, Used answer[-4:] to show only the last 4 digits.