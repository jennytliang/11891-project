def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""


    retur = 0
    while string[retur] != '\0':
        retur += 1
    return retur


if __name__ == '__main__':
    import doctest
    doctest.testmod()
