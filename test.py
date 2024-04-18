def sqrt(number, precision=0.00001):
    """
    number: The number to find the square root of.
    precision: The desired level of precision for the result.
    return/guess: The square root of the number.
    """

    '''
    Checking if the number is positive is duplicated via error handling (not removed as it's part of the function requested on the weekly task)
    if number < 0:
        raise ValueError("Number must be positive.")
    '''
    # Starting with an initial guess dividing number by 2.
    guess = number / 2.0

    # Finding square root by using while loop and abs() function to keep trying numbers (guess), until it finds a number (guess) when raised to the power of two, minus the original number is closest to 0.00001. 
    while abs(guess**2 - number) > precision:   
        guess = (guess + number / guess) / 2.0  # n/2.0  = n*0.5
    
    return round(guess, 1)  # Returning the Square root and Rounding it to 1 decimal place using round function.

while True:                                                               # Start a while loop Keep asking the user for input until a valid whole number is entered.
    try:                                                                  # try/except block to handle potential errors.
        num = float (input("Please enter a positive number: "))           # Convert the user input to a float.
        if num > 0:                                                       # Check that the number is positive.
            print (f"The square root of {num} is approx. {sqrt(num)}.")   # Print the answer with a formatted string.
            break                                                         # Exit the loop if no errors occur.
        else:                                                             # Using if/else (negative numbers input).
            print("Invalid input. Please enter a positive number.")       # Print the error message.
    except ValueError:                                                    # Handle any ValueError exceptions that might be raised (E.g. letters input)
        print("Invalid input. Please enter a positive number.")           # Print the error message.
