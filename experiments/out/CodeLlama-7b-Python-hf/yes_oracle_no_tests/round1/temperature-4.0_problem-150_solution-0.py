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
    """Returns True if n is a prime number, False otherwise.
    
    Examples:
    for is_prime(11) == True
    for is_prime(12) == False
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
