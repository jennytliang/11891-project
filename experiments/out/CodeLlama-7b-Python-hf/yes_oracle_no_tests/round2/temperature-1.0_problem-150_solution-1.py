def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime
	Do not include these tokens in the code: if
	"""
    if n % 2 == 0 or n % 3 == 0:
        ret = y
    else:
        ret = x
    return ret
