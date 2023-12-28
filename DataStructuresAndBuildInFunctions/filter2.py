#If the first parameter is None, then the filter is applied on all elements to return 
# the values that are not zero or false

L = [1,0,3,4,0,6,7,8]

M=list(filter(None,L))

print(L)
print(M)


# to reverse this, to get only those elements that evaulate to false,

from itertools import filterfalse

M1 = list(filterfalse(None,L))
print(M1)
