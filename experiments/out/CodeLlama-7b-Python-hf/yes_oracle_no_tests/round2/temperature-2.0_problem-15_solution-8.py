def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: map (
	"""



    
    retu = ""
    for i in range(0,n+1):
        retu += str(i) + " "
    return retu



if __name__ == "__main__":
    import doctest
    doctest.testmod()
