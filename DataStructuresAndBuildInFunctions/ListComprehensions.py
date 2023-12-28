# list comprehensions are powerful.
# they can combine all operations map(), reduce(), filter() used in marksAnalyzer.py in single step.

L = [1,6,4,9,7]
M = [2*x for x in L]
print("getting the 2*x")
print(M)


# implementing filter

L = [1,6,4,9,7]
M = [x for x in L if x%2 == 0]
print("filtering only the even numbers")
print(M)

# Combining Map and filter
L = [1,6,4,9,7]
M = [x*x for x in L if x%2==0]
print("Combining map and filter")
print(M)


# Getting all prime numbers
def isPrime(n):
    for i in range(2,n):
        if n%i == 0: return False
    else:
        return True

p = [x for x in range(2,100) if isPrime(x)]
print("prime numbers less than 100")
print(p)

# excluding prime numbers that end with 9
p1 = [x for x in range(2,100) if isPrime(x) if not x%10==9]
print("Prime numbers except the ones ending with 9")
print(p1)