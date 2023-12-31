# Exception handling demo
# Common handling of Multiple exceptions

try:
    n = int(input("Enter an integer:"))
    result = int(100/n)
    print("100/{} = {}".format(n, result))

except(ValueError,ZeroDivisionError):
    print("Unable to calculate!")

print("exiting the program")