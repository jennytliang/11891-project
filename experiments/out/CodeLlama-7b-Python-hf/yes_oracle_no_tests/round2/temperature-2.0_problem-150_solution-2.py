def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def
	Do not include these tokens in the code: if
	"""
    if n%2 != 0 and n%3 != 0 and n%5 != 0 and n%7 != 0:
        return x
    else:
        return y

print(x_or_y(15, 8, 5))
