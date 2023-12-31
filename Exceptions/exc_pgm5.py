# Exception handling demo
# using else and finally

try:
    n = int(input("Enter an integer:"))
    result = int(100/n)
except:
    print("Sorry..Unable to calculate..")
else:
    print("100/{} = {}".format(n, result))
finally:
    print("exiting the program..finally")
