# Write a method in python that will create two separate text files after reading the source text file 
# named integers.txt that contains 20 integers. The first output file will be named double.txt 
# containing the square of all even integers found in integers.txt and the second file will be 
# named triple.txt containing the cube of all odd numbers found in the integers.txt.

import pyfiglet
import time
# Defining variable
intro = pyfiglet.figlet_format("WELCOME".center(39, "="), font = "digital")
# Welcome message and its function
print(intro)
print("\033[44;1m" + "This program will create two text file, double.txt and triple.txt, that respectively contains the sqaures of all even numbers and the cubes of all odd numbers extracted from a file text named numbers.txt.\n" + "\033[0m")
input("Press the ENTER key to run the program....\n")
time.sleep(5)
# Open the input file and read the numbers
with open("integers.txt", "r") as input_file:
    numbers = input_file.readlines()
# Convert the numbers to integers
numbers = [int(num) for num in numbers]

# Extract even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
    double_file.write("These are the squares of all even integers in the file:" + "\n")
    # Write the squares of even numbers to double.txt
    for num in even_numbers:
        numbers = double_file.write(str(num**2) + "\n")
    triple_file.write("These are the cubes of all odd integers in the file:" + "\n")
    # Write the cubes of odd number to odd.txt
    for num in odd_numbers:
        numbers = triple_file.write(str(num**3) + "\n")
# Display the confirmation message