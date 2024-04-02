def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    pass


# tests
if __name__ == '__main__':
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(16, 34, 12) == 12
    assert x_or_y(1, 34, 12) == 12