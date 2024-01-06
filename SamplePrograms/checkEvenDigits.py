# Check if all the digits in a number are even

"""
This program checks if all the digits in a number are even.

>>> checkEvenDigit(0)
True

>>> checkEvenDigit(100)
False

>>> checkEvenDigit(5846)
False

>>> checkEvenDigit(25)
False

>>> checkEvenDigit(9870)
False

>>> checkEvenDigit(2648)
True


"""

def checkEvenDigit(n):
    while n > 0:
        if n%2 == 1:
            return False
        n = n // 10
    return True   
    


if __name__ == "__main__":
    import doctest
    doctest.testmod()
   