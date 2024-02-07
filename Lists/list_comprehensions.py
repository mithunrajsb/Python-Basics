"""
List comprehensions provide a concise way to create lists, which is beneficial for both readability and,
 in many cases, performance. It reduces the need for multi-line loops.

 Use list comprehensions when you want to transform or filter data, particularly when the logic is simple. 
 They’re suitable for small operations on data sets.


"""

# If we need to find squares of all even numbers in a range, we can use:


squares = [x**2 for x in range(10) if x % 2 == 0]

print(squares)
