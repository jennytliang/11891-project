def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    return x if is_prime(n) else y

def is_prime(n):
    """This function determines whether or not a number is prime.
    
    Examples:
    for is_prime(15) == False
    for is_prime(17) == True
    for is_prime(19) == True
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(x_or_y(15, 8, 5)) # Should be 5
print(x_or_y(7, 34, 12)) # Should be 34
print(x_or_y(19, 8, 5)) # Should be 8
print(x_or_y(15, 8, 5)) # Should be 5
print(x_or_y(17, 8, 5)) # Should be 8