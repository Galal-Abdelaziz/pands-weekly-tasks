# es.py
# Weekly Tasks 07
# This program reads in a text file from an argument on the command line and outputs the number of e's it contains.
# Also checks if it is an existing file, text file, and regular file, If any of these checks fail, the program prints an error message and exits with a non-zero exit code.
# author: Galal Abdelaziz
# test code "python es.py moby-dick.txt"

import argparse                       # Import the argparse module for parsing command line arguments.
import os                             # Import the os module for file operations.

def count_e(filename: str) -> int:    # Function used to count the number of times 'e' appears in the file with the given filename, takes a filename as a string argument and returns an integer.

    with open(filename, 'r') as file:  # Open the file in read mode ('r')
        text = file.read()             # Read the contents of the file into the variable 'text'        
        num_e = text.count('e')        # Count the number of times the letter 'e' appears in the text       
        return num_e                   # Return the number of times the letter 'e' appears in the text

def main():      # Parse command line arguments, check if the file exists and is a text file, and print the number of times 'e' appears in the file.
   
    parser = argparse.ArgumentParser(description='Count the number of times "e" appears in a file.')  # Set up command line argument parser
    parser.add_argument('filename', type=str, help='The name of the file to analyze.')                # Define the filename argument
    args = parser.parse_args()                                                                        # Parse the command line arguments

    if not os.path.exists(args.filename):                                                      # Check if the file exists
        print(f"Error: The file '{args.filename}' does not exist.")
        return 1                                                                               # Return an error code (1) (Main function exit status)
 
    if not os.path.isfile(args.filename):                                                       # Check if the file is a regular file
        print(f"Error: The file '{args.filename}' is not a regular file.")
        return 1                                                                                # Return an error code (1) (Main function exit status)

    if not os.path.splitext(args.filename)[-1].lower() in ('.txt', '.text', '.utf8', '.utf-8'):  # Check if the file is a text file
        print(f"Error: The file '{args.filename}' is not a text file.")
        return 1                                                                                 # Return an error code (1) (Main function exit status)

    num_e = count_e(args.filename)            # Call the count_e function with the filename from the command line 'filename' argument

    print(f"The letter 'e' appears {num_e} times in the file {args.filename}.")  # Print the result, using an f-string to format the output message
    return 0                                                                                      # Return a success code (0) (Main function exit status)

if __name__ == "__main__":
    exit(main())                                                                       # Exit the program with the return code from the main function