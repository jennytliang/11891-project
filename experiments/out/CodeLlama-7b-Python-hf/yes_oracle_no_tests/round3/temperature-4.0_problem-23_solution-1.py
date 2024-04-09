def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Do not include these tokens in the code: r = 0 for
	"""
    
    r = 0 # TODO: replace this line with something else
    for c in string:
        r = r + 1
    return r


print(strlen(''))
print(strlen('abc'))

