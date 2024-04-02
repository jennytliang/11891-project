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
    """This function returns True if n is prime, False otherwise.

	Examples:
	for is_prime(10) == False
	for is_prime(7) == True
	for is_prime(14) == False
	"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def print_x_y(x, y):
    """This function should print the values of x and y.

	Examples:
	for print_x_y(34, 12) == 34 12
	for print_x_y(8, 5) == 8 5
	"""
    print(x, y)


print_x_y(x_or_y(7, 34, 12), x_or_y(15, 8, 5))
