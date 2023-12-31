# Exception handling demo
# Exception instances

try:
    n = int(input("Enter an integer:"))
    result = int(100/n)
    print("100/{} = {}".format(n, result))
except Exception as e:
    print("Unable to calculate!")
    print("Details: ",e)

print("exiting the program")