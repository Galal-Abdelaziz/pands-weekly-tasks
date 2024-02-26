# weekday.py
# Weekly Tasks 05
# This program outputs whether or not today is a weekday.
# author: Galal Abdelaziz

import datetime                                        # Impoting datetime module (built in Python).

day = datetime.datetime.today().weekday()              # setting up the variable to include the following tuples from the module, today (the day of runnding the script) and weekday (0-6 = Mon-Sun).

if day < 5:                                            # using if / else statment (<5) (0 Mon- 4 Fri).
    print ("Yes, unfortunately today is a weekday.")   # Printing the weekday statment (string).
else:                                                  # using if / else statment  (5 Sat, 6 Sun).
    print ("It is the weekend, yay!")                  # Printing the weekend statment (string).