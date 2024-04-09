def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: +
	"""

    return " ".join(map(str, rage(0, n + 1)))


def rage(start: int, stop: int) -> list[int]:
    """ Return a list of integers from start to stop.
    >>> rage(0, 3)
    [0, 1, 2, 3]
    >>> rage(3, 0)
    [3, 2, 1, 0]
    """

    return list(range(start, stop + 1))
