def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    return x if is_prime(n) else y


def is_prime(n):
    """Helper function to check if a number is prime"""
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


assert x_or_y(7, 34, 12) == 34
assert x_or_y(15, 8, 5) == 5
assert x_or_y(10, 34, 12) == 12
assert x_or_y(15, 34, 12) == 12
assert x_or_y(100, 34, 12) == 12
assert x_or_y(150, 34, 12) == 12
assert x_or_y(300, 34, 12) == 12
