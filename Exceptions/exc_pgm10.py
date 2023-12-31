# User defined exceptions with arguments

class OverflowException(Exception):
    def __init__(self, value) :
        self._value = value
    def getValue(self):
        return self._value
    
class NegativeInputException(Exception):
    def __init__(self, value) :
        self._value = value
    def getValue(self):
        return self._value

def check(n):
    if n>100:
        raise OverflowException(n)
    if n<0:
        raise NegativeInputException(n)


try:
    n=int(input("Enter an integer :"))
    check(n)
    result = int(100/n)
    print("100/{} = {}".format(n, result))

except OverflowException as e:
    print("The given input ({}) is too large!".format(e.getValue()))
    print("Pleae enter an integer less than 100!")

except NegativeInputException as e:
    print("The given input ({}) is negative!".format(e.getValue()))
    print("Please do not enter a negative number!")

except ValueError:
    print("Please enter an integer")

except ZeroDivisionError:
    print("Sorry! Division by zero is not permitted!")

print("Thanks for using this program")