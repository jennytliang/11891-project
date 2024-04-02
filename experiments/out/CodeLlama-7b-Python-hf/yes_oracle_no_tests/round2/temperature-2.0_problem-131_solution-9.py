def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	"""
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = res * (n % 10)
        n = n // 10
    return res


def digits2(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	"""
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = res * (n % 10)
        n = n // 10
    return res


def digits3(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	"""
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = res * (n % 10)
        n = n // 10
    return res


def digits4(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 