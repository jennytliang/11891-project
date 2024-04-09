def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: str
	"""



    retu = 0
    for i in string:
        if i == '\0':
            break
        else:
            retu += 1
    return retu


if __name__ == "__main__":
    import doctest
    doctest.testmod()