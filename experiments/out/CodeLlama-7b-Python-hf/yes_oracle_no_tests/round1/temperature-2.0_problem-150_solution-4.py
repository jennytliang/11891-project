def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    if is_prime(n):
        return x
    else:
        return y


def is_prime(n):
    """
    This function returns True if n is prime, False otherwise.
    """
    if n <= 2:
        return False
    elif n % 2 == 0 and n != 2:
        return False
    else:
        for i in range(3, n):
            if n % i == 0:
                return False
        return True


print(x_or_y(7, 34, 12))  # should print 34
print(x_or_y(15, 8, 5))  # should print 5
