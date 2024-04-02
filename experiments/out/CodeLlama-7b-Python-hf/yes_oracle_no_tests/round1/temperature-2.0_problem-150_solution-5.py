def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    prime = 0
    if is_prime(n):
        prime = x
    else:
        prime = y
    return prime


def is_prime(n):
    """
    Checks if n is a prime number
    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    >>> is_prime(20)
    False
    >>> is_prime(25)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))
# print(x_or_y(10, 34, 12))
# print(x_or_y(15, 8, 5))
