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
    """Returns whether or not the given number is prime.

    Examples:
    for is_prime(7) == True
    for is_prime(15) == False
    
    Include these tokens in the code: if _ % _ == _:
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
