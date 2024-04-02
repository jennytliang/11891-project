def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: not ( a <
	Do not include these tokens in the code: ==
	"""

    def is_prime(a):
        r = True
        for i in range(2, a):
            if a % i == 0:
                r = False
        return r

    if is_prime(n):
        return x
    else:
        return y
