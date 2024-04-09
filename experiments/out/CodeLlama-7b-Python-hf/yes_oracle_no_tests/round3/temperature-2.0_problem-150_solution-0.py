def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    if not is_prime(n):
        return y
    else:
        return x


def is_prime(n):
    """
    This function should return True if n is prime and False otherwise.
    
    Examples:
    is_prime(7) == True
    is_prime(8) == False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
