def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def
	Do not include these tokens in the code: if
	"""
    if n % 2 == 0:
        return y
    else:
        return x


def x_and_y(n, x, y):
    """A simple program that should return the value of x if n is
    a prime number and should return the value of y otherwise.

    Examples:
    for x_and_y(7, 34, 12) == 12
    for x_and_y(15, 8, 5) == 8
    
    Include these tokens in the code: def
    Do not include these tokens in the code: if
    """
    if n % 2 == 0:
        return x
    else:
        return y


def x_plus_y(n, x, y):
    """A simple program that should return the sum of x and y if n is
    a prime number and should return the product of x and y otherwise.

    Examples:
    for x_plus_y(7, 34, 12) == 46
    for x_plus_y(15, 8, 5) == 40
    
    Include these tokens in the code: def
    Do not include these tokens in the code: if
    """
    if n % 2 == 0:
        return x * y
    else:
        return x + y
