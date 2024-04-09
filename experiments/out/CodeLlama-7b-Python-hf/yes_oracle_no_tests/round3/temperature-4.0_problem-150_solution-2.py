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
    """A simple program which should return True if n is a prime number and
    False otherwise.

    Examples:
    for is_prime(7) == True
    for is_prime(8) == False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 1. What is the value of x_or_y(15, 8, 5)?
# 2. What is the value of x_or_y(7, 34, 12)?
# 3. What is the value of x_or_y(15, 34, 5)?
# 4. What is the value of x_or_y(15, 34, 12)?
# 5. What is the value of x_or_y(15, 34, 34)?
# 6. What is the value of x_or_y(15, 8, 12)?