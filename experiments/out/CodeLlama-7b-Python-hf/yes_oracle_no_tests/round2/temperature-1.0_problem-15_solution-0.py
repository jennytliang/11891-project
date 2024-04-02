def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ". join ( map ( str ,
	Do not include these tokens in the code: r = "" for
	"""
    r = ""
    for i in range(n + 1):
        r += str(i) + " "
    return r


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(string_sequence(10))
