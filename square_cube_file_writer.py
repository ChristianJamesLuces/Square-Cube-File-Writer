# Write a method in python that will create two separate text files after reading the source text file 
# named integers.txt that contains 20 integers. The first output file will be named double.txt 
# containing the square of all even integers found in integers.txt and the second file will be 
# named triple.txt containing the cube of all odd numbers found in the integers.txt.


# Open the input file and read the numbers
with open("integers.txt", "r") as input_file:
    numbers = input_file.readlines()
# Convert the numbers to integers
numbers = [int(num) for num in numbers]
# Extract even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
# Write the squares of even numbers to double.txt
# Write the cubes odd number to odd.txt
# Display the confirmation message