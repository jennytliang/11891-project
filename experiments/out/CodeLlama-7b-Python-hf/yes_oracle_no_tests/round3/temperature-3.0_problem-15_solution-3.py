def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: +
	"""

    return " ".join(map(str, rage(n+1)))


def range(n: int) -> list:
    """Return a list containing numbers starting from 0 upto n inclusive.

    >>> range(3)
    [0, 1, 2, 3]
    >>> range(5)
    [0, 1, 2, 3, 4, 5]
    """

    return list(range(n+1))


# Manually written version of range
def rage(n: int) -> list:
    """Return a list containing numbers starting from 0 upto n inclusive.

    >>> rage(3)
    [0, 1, 2, 3]
    >>> rage(5)
    [0, 1, 2, 3, 4, 5]
    """

    result = []
    for i in range(n+1):
        result.append(i)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
