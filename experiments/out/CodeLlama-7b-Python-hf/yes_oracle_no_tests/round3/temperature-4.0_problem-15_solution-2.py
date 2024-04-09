def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: +
	"""

    return " ".join(map(str, rage(n+1)))

def rage(n: int) -> list:
    """ Return a list of numbers from 0 up to n inclusive.
    >>> rage(3)
    [0, 1, 2, 3]
    """

    return list(range(n+1))

if __name__ == "__main__":
    import doctest
    doctest.testmod()