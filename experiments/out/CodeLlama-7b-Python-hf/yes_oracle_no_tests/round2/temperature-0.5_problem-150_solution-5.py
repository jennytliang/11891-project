def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    pass


def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y
