def product(a, b):
    """
    This function adds two numbers.

    >>> product(7, 3)
    21
    >>> product(-1, 1)
    -1
    >>> product(-1, -6)
    6

    >>> product(0,897)
    0
    """
    return a * b

if __name__ == "__main__":
    import doctest

    # Run tests defined in docstrings using doctest
    doctest.testmod()
