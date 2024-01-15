def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
    

def numbers_to_digits(number):
    # Convert the number to a string and then to a list of integers
    digits = [int(digit) for digit in str(abs(number))]

    return digits

if __name__ == "__main__":
    curious_numbers = []
    # Considering that the curious numbers are in range from 1 to 9999999
    for i in range(3,9999999):
        digits = numbers_to_digits(i)
        # Get the sum of factorials of the digit
        sum = 0
        for d in digits:
            sum += fact(d)
        if sum == i:
            curious_numbers.append(i)
    print("The numbers are : ",curious_numbers)
    print(sum(curious_numbers))
    
    

