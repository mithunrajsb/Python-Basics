# Raising exceptions
# Exceptions from functions

def divideAndPrint():
    try:
        n=int(input("Enter an integer :"))
        result = int(100/n)
        print("100/{} = {}".format(n, result))

    except ValueError:
        print("Please enter an integer !")


try:
    divideAndPrint()

except ValueError:
        print("Invalid value !")
except ZeroDivisionError:
    print("Sorry! Division by zero is not permitted!")