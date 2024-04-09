def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: +
	"""

    return " ".join(map(str, rage(0, n+1)))


def rage(m: int, n: int) -> list:
    """ Return a list of all numbers between m and n inclusive.
    >>> rage(2, 4)
    [2, 3, 4]
    >>> rage(10, 12)
    [10, 11, 12]
    """

    return list(range(m, n+1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
