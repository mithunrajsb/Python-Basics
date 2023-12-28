# The reduce function reduces a sequence to a single value

from functools import reduce
def f(x,y):
    return x + y

L = [1,6,4,9,7,8]
sum = reduce(f,L)
print(sum)


# to return the product of all elements

def f(x,y):
    return x * y

L = [1,2,3,4,9,8]
pdct = reduce(f,L,2)  #multiplies by 2 also
print(pdct)