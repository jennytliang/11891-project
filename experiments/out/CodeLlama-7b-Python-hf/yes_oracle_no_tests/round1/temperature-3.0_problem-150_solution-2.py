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
    """
    return True if n is prime, otherwise return False
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))
