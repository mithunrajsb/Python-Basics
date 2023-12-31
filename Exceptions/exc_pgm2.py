# Exception handling demo
# Multiple exceptions

try:
    n = int(input("Enter an integer:"))
    result = int(100/n)
    print("100/{} = {}".format(n, result))

except ValueError:
    print("Invalid input! Please enter an integer")

except ZeroDivisionError:
    print("Sorry..Division by zero not permitted..")
print("exiting the program")