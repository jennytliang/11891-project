def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # write your code
	"""
    if n % y == 0 or n % x == 0:
        return y
    else:
        return x


print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))
