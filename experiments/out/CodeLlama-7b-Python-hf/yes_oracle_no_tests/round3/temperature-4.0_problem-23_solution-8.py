def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""


    returnt = 0
    for i in string:
        returnt += 1
    return returnt

if __name__ == "__main__":
    import doctest
    doctest.testmod()