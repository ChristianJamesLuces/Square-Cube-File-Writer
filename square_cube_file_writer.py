# Write a method in python that will create two separate text files after reading the source text file 
# named integers.txt that contains 20 integers. The first output file will be named double.txt 
# containing the square of all even integers found in integers.txt and the second file will be 
# named triple.txt containing the cube of all odd numbers found in the integers.txt.


# Open the input file and read the numbers
with open("integers.txt", "r") as input_file:
    numbers = input_file.readlines()
# Convert the numbers to integers
numbers = [int(num) for num in numbers]

with open("dounble.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
    double_file.("These are the squares of all even integers in the file:" + "\n")
    # Write the squares of even numbers to double.txt
    for num in numbers:
        if num % 2 == 0:
            numbers = double_file.write(str(num**2) + "\n")
    # Write the cubes of odd number to odd.txt
    for num in numbers:
        if num % 2 != 0:
            numbers = triple_file.write(str(num**3) + "\n")
# Display the confirmation message