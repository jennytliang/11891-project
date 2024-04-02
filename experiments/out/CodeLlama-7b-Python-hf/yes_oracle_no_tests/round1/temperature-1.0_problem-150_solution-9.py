def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    if n <= 1:
        return y
    elif n in [3, 5]:
        return x
    elif n % 2 == 0 or n % 3 == 0:
        return y
    else:
        prime = False
        for i in range(10):
            x = 2 * x + y
            if is_prime(x):
                if (x % 2 != 0 and x % 3 != 0) or (x % 5 != 0 and x % 7 != 0):
                    prime = True
                    break
        
        if prime:
            return x
        else:
            return y
