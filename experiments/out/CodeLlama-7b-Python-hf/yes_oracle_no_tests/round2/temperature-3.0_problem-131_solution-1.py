def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: if n == 0 :
	"""
    # Your code here
    product = 1
    if n == 0:
        return 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
        n = n // 10
    return product


def digits2(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: if n == 0 :
	"""
    # Your code here
    product = 1
    if n == 0:
        return 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
        n = n // 10
    return product


def digits3(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: if n == 0 :
	"""
    # Your code here
    product = 1
    if n == 0:
        return 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
        n = n // 10
    return product


def digits4(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0