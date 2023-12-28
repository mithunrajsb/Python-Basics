# Use of map(), filter() and reduce() using lambda expressions

L = [1,6,4,9,7]
M = list(map(lambda x: x**2,L))
print(M)


# To filter out the odd integers and allow only the even numbers in the list,
L = [1,2,5,6,7,87,34]
M = list(filter(lambda x: x%2==0,L))
print(M)


# To add all elements in a list
from functools import reduce
L = [1,2,4,5,6,7,8]
sum=reduce(lambda x,y:x+y,L)
print(sum)