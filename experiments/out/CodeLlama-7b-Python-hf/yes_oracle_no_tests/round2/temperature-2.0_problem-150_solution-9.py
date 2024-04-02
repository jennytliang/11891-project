def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    # code goes here
    
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    """Return True if n is a prime number or False otherwise."""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(x_or_y(7, 34, 12))
    # 34
    print(x_or_y(15, 8, 5))
    # 5
