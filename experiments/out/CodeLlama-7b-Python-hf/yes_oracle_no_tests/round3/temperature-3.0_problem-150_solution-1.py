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
    """Check if n is a prime number.

    Examples:
    for is_prime(7) == True
    for is_prime(9) == False
    for is_prime(11) == True
    """
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_while(n):
    """Check if n is a prime number (using while loop).

    Examples:
    for is_prime(7) == True
    for is_prime(9) == False
    for is_prime(11) == True
    """
    if n % 2 == 0:
        return False
    i = 3
    while i < int(n**0.5) + 1:
        if n % i == 0:
            return False
        i = i + 2
    return True


def is_prime_for(n):
    """Check if n is a prime number (using for loop).

    Examples:
    for is_prime(7) == True
    for is_prime(9) == False
    for is_prime(11) == True
    """
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
