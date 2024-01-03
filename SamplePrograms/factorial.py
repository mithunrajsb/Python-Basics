# Write a program to return the factorial of a given number

"""
This is a function to return the factorial of a given number

>>> fact(3)
6

>>> fact(5)
120

>>> fact(0)
1

>>> fact(10)
3628800

"""

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
    

if __name__ == "__main__":
    import doctest
    import timeit
    import sys
    doctest.testmod()

    print(sys.getrecursionlimit())  # Checking the system recursion limit . By default it is 1000. fact(1024) will fail.
                                    # RecursionError: maximum recursion depth exceeded

    sys.setrecursionlimit(5000)  # Setting the system recursion limit to 5000.

    print(sys.getrecursionlimit()) 
    inputs = [5, 10, 15, 20, 256, 800, 4096]

    for num in inputs:
        # Construct the statement to test with timeit
        stmt = f"fact({num})"
        
        # Measure the execution time for the factorial function with current input
        execution_time = timeit.timeit(stmt, globals=globals(), number=10000)
        
        print(f"Factorial of {num}: Execution time = {execution_time:.6f} seconds")
