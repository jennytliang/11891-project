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
    """A simple program which should return True if n is a prime number
    and False otherwise.

    Examples:
    for is_prime(7) == True
    for is_prime(15) == False
    
    Include these tokens in the code: def is_prime ( a ): return
    """
    return False


def add(a, b):
    """A simple program which should return the sum of a and b.

    Examples:
    for add(10, 20) == 30
    for add(10, 30) == 40
    
    Include these tokens in the code: def add ( a, b ): return
    """
    return a + b


def add_three(a, b, c):
    """A simple program which should return the sum of a, b and c.

    Examples:
    for add_three(10, 20, 30) == 60
    for add_three(10, 30, 40) == 100
    
    Include these tokens in the code: def add_three ( a, b, c ): return
    """
    return a + b + c


def multiply(a, b):
    """A simple program which should return the product of a and b.

    Examples:
    for multiply(10, 20) == 200
    for multiply(10, 30) == 300
    
    Include these tokens in the code: def multiply ( a, b ): return
    """
    return a * b


def multiply_three(a, b, c):
    """A simple program which should return the product of a, b and c.

    Examples:
    for multiply_three(10, 20, 30) == 6000
    for multiply_three(10, 30, 40) == 