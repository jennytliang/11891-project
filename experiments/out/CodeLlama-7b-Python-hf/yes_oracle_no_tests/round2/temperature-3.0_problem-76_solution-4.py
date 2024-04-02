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
    return x == n**int(n)


def is_simple_power_v2(x, n):
    """
    return n**int(log(x, n)) == x
    """
    return n**int(log(x, n)) == x


def log(x, n):
    """
    log_n(x) = log(x) / log(n)
    """
    return log(x) / log(n)


def log2(x):
    """
    log2(x) = log(x) / log(2)
    """
    return log(x) / log(2)


def log10(x):
    """
    log10(x) = log(x) / log(10)
    """
    return log(x) / log(10)


def log16(x):
    """
    log16(x) = log(x) / log(16)
    """
    return log(x) / log(16)


def log3(x):
    """
    log3(x) = log(x) / log(3)
    """
    return log(x) / log(3)


def log5(x):
    """
    log5(x) = log(x) / log(5)
    """
    return log(x) / log(5)


def log7(x):
    """
    log7(x) = log(x) / log(7)
    """
    return log(x) / log(7)


def is_simple_power_v3(x, n):
    """
    return int(log(x, n)) == log(x, n)
    """
    return int(log(x, n)) == log(x, n)


def is_simple_power_v4(x, n):
    """
    return int(log(x, n)) == log(x, n)
    """
    return int(log(x, n)) == log(x, n)
