def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""

    # write code here
    def is_prime(a):
        if a == 1:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y


print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))
