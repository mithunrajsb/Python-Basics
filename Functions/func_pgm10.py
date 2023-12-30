# Documentation strings

def isPrime(n):
    """Returns whether n is prime or not.
    
    Given a non-negative integer n, this function
    returns True if n is prime and False otherwise.
    The argument n is assumed to be a positive integer 
    greater than 1(since 1 is neither prime nor composite).
    """

    for i in range(2,int(n/2)+1):
        if n%i==0: return False
    return True


print(isPrime.__doc__)