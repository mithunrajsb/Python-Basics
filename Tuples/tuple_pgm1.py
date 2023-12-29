# A Tuple is defined as an immutable ordered sequence of elements

T = tuple([12,15,18])
print(T)

#Accessing a tuple element
print(T[1])

# print(T[4])  # Index out of range error

#Elements cannot be changed
# T[0] = 50  # TypeError: 'tuple' object does not support item assignment
print(T[0])

# Iterating through Tuple elements
for i in T:
    print(i)