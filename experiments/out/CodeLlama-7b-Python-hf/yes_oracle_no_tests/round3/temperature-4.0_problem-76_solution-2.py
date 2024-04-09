def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    
	Include these tokens in the code: if x ==
	"""
    
    # If n is 1, then x is a simple power of n iff x == 1
    if n == 1:
        return x == 1
    # If x is not a power of n, then x is not a simple power of n
    if x % (n**int(x/n)) != 0:
        return False
    # If x is a power of n, then x is a simple power of n iff
    # x == n**int(x/n)
    return x == n**int(x/n)