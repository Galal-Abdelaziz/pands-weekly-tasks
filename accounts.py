#accounts.py
#Weekly Tasks 03
#reads in any length account number and outputs the account number with only the last 4 digits showing.
#author: Galal Abdelaziz

answer = input("Please enter an 10 digit account number:")

'''
#can use this code to restrict input to 10 digits
if len(answer) != 10:
        print ("Please enter 10 digits")
if len(answer) == 10:

        print ("x" * (len(answer) - 4) + answer[-4:])
'''
print ("x" * (len(answer) - 4) + answer[-4:])