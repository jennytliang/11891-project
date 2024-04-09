def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Do not include these tokens in the code: ret ur = 0
	"""
    ur = 0
    for i in string:
        ur += 1
    return ur