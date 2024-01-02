def add(a, b):
    """
    This function adds two numbers.

    >>> add(7, 3)
    10
    >>> add(-1, 1)
    0
    >>> add(0.5, 0.5)
    1.0
    """
    return a + b

if __name__ == "__main__":
    import doctest

    # Run tests defined in docstrings using doctest
    doctest.testmod()
