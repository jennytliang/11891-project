def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: if n > 1 :
	"""

    xor=0
    if is_prime(n):
        xor=x
    else:
        xor=y
    
    return xor
    
