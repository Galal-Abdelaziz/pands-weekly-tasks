# squareroot.py
# Weekly Tasks 06
# This program takes a positive floating-point number as input and outputs an approximation of its square root using Newton's method.
# author: Galal Abdelaziz

def sqrt(number, precision=0.00001):
    """
    number: The number to find the square root of.
    precision: The desired level of precision for the result.
    return/guess: The square root of the number.
    """

    # Check that the number is positive.
    if number <= 0:
        raise ValueError("Number must be positive.")

    # Starting with an initial guess dividing number by 2.
    guess = number / 2.0

    # Finding square root by using while loop and abs() function to keep trying numbers (guess), until it finds a number (guess) when raised to the power of two, minus the original number is closest to 0.00001. 
    while abs(guess**2 - number) > precision:   
        guess = (guess + number / guess) / 2.0
    
    return round(guess, 1)  # Returning the Square root and Rounding it to 1 decimal place using round function.



num = float (input("Please enter a positive number: "))
print (f"The square root of {num} is approx. {sqrt(num)}.")

