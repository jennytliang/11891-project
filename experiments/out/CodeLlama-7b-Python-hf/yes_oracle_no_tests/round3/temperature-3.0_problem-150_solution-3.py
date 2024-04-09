def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    
    if is_prime(n):
        return x
    else:
        return y
    
    
def is_prime(n):
    """Returns True if n is a prime number.
    
    Examples:
    is_prime(3) == True
    is_prime(7) == True
    is_prime(11) == True
    is_prime(15) == False
    """
    
    for d in range(2, n):
        if n % d == 0:
            return False
    
    return True
