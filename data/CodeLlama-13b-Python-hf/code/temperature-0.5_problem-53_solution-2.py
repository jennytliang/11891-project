def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y


def subtract(x: int, y: int):
    """Subtract x from y
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
    """
    return y - x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
