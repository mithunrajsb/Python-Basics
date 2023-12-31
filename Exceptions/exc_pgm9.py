# User defined exceptions

class OverflowException(Exception):
    pass

class NegativeInputException(Exception):
    pass

def check(n):
    if n>100:
        raise OverflowException()
    if n<0:
        raise NegativeInputException()


try:
    n=int(input("Enter an integer :"))
    check(n)
    result = int(100/n)
    print("100/{} = {}".format(n, result))

except OverflowException:
    print("Please enter an integer less than 100!")

except NegativeInputException:
    print("Please do not enter a negative number!")

except ValueError:
    print("Please enter an integer")

except ZeroDivisionError:
    print("Sorry! Division by zero is not permitted!")

print("Thanks for using this program")