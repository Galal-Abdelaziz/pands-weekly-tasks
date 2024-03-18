# es.py
# Weekly Tasks 07
# This program reads in a text file from an argument on the command line and outputs the number of e's it contains.
# author: Galal Abdelaziz
# test code "python es.py moby-dick.txt"

import argparse # Import the argparse module for parsing command line arguments.

def count_e(filename): #function used to count the number of times 'e' appears in the file with the given filename.
    
    with open(filename, 'r') as file: # Open the file in read mode ('r').
        text = file.read() # Read the entire contents of the file into a string.
        num_e = text.count('e') # Count the number of times 'e' appears in the string.
        return num_e # Return the count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of times "e" appears in a file.')   # Set up command line argument parser.
    parser.add_argument('filename', type=str, help='The name of the file to analyze.') # Define the filename argument.
    args = parser.parse_args()  # Parse the command line arguments.

    num_e = count_e(args.filename) # Call the count_e function with the filename from the command line argument.

    print(f"The letter 'e' appears {num_e} times in the file {args.filename}.") # Print the result, using an f-string to format the output message. 
    # The {num_e} and {args.filename} placeholders are replaced with their values.