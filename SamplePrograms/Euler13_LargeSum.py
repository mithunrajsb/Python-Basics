# First 10 digits of the sum of One Hundred 50 digit numbers
# Read the input(50 numbers from a file). Separate the 50 digit numbers from the input
# Get the sum
# Find the first 10 digits

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Get the first 10 digits
first_ten_digits = str(total_sum)[:10]
print("First 10 digits of the sum: ",first_ten_digits)
print("Total Sum is :{}, It is a {} digit number ".format(total_sum,len(str(total_sum))))