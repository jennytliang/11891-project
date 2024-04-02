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
    """Checks if a number is prime.

    Examples:
    is_prime(7) == True
    is_prime(8) == False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def x_or_y_solution(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    return x if is_prime(n) else y


def is_prime(n):
    """Checks if a number is prime.

    Examples:
    is_prime(7) == True
    is_prime(8) == False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def x_or_y_solution(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    return x if is_prime(n) else y
