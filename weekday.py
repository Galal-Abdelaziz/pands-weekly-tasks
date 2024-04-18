# weekday.py
# Weekly Tasks 05
# This program outputs whether or not today is a weekday.
# author: Galal Abdelaziz

'''
This is the code with no error handling
import datetime                                        # Impoting datetime module (built in Python).
day = datetime.datetime.today().weekday()              # setting up the variable to include the following tuples from the module, today (the day of runnding the script) and weekday (0-6 = Mon-Sun).
if day < 5:                                            # using if / else statment (<5) (0 Mon- 4 Fri).
    print ("Yes, unfortunately today is a weekday.")   # Printing the weekday statment (string).
else:                                                  # using if / else statment  (5 Sat, 6 Sun).
    print ("It is the weekend, yay!")                  # Printing the weekend statment (string).
'''

import datetime                                            # Importing datetime module (built in Python).

try:                                                       # try/except block to handle potential errors.
    day = datetime.datetime.today().weekday()              # Setting up the variable to include the following tuples from the module, today (the day of runnding the script) and weekday (0-6 = Mon-Sun).

    if day < 5:                                            # Using if / else statment (<5) (0 Mon- 4 Fri).
        print ("Yes, unfortunately today is a weekday.")   # Printing the weekday statment (string).
    else:                                                  # Using if / else statment  (5 Sat, 6 Sun).
        print ("It is the weekend, yay!")                  # Printing the weekend statment (string).
except Exception as e:                                     # This error is raised when an unexpected exception occurs.
    print(f"An error occurred: {e}")                       # Print the error message.