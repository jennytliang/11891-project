def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return len(string)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
