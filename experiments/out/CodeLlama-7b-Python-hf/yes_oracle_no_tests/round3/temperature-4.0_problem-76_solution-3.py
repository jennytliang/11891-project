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
    return x == n ** int(x / n)


def is_simple_power_2(x, n):
    """Write a function that returns true if a number x is a simple power of n and
    false in other cases.

    x is a simple power of n if n**int=x

    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false

    """
    return x == n ** int(math.log(x) / math.log(n))


def is_simple_power_3(x, n):
    """Write a function that returns true if a number x is a simple power of n and
    false in other cases.

    x is a simple power of n if n**int=x

    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false

    """
    return x == n ** int(math.log(x) / math.log(n))


def is_simple_power_4(x, n):
    """Write a function that returns true if a number x is a simple power of n and
    false in other cases.

    x is a simple power of n if n**int=x

    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
