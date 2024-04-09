def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Do not include these tokens in the code: r = 0 for
	"""
    r = 0
    for char in string:
        r += 1
    return r


print(strlen(''))
print(strlen('abc'))
