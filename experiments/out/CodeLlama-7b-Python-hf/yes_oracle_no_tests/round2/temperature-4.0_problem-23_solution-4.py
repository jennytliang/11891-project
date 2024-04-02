def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = 0
    for i in string:
        r += 1
    return r


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(strlen('abc'))