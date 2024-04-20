def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Do not include these tokens in the code: # solution target
	"""
    result = ''
    for i in range(n + 1):
        result += str(i) + ' '
    return result[:-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()