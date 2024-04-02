def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if a == 0 :
	"""
    ''' [YOUR CODE HERE] '''
    if a == 0 or b == 0:  # the program can run for a while if we don't do this check
        raise ValueError('one of the integers passed in must not equal zero')
    if a > b:
        return greatest_common_divisor(b, a)
    if a == b:
        return a
    return greatest_common_divisor(a, b - a)
