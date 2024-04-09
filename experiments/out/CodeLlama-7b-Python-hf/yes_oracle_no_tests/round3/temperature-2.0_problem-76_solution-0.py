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
    return pow(n, int(x/n)) == x


def is_simple_power_v2(x, n):
    """
    This is an alternative solution.
    """
    return (x % n == 0) and (x / n == n)


def is_simple_power_v3(x, n):
    """
    This is an alternative solution.
    """
    return (x % n == 0) and (x / n == int(x / n))


def is_simple_power_v4(x, n):
    """
    This is an alternative solution.
    """
    return (x % n == 0) and (x / n == n) and (x / n == int(x / n))


def is_simple_power_v5(x, n):
    """
    This is an alternative solution.
    """
    return (x % n == 0) and (x / n == int(x / n)) and (x / n == n)
