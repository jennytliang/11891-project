def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    # your code here
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod


def digits2(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    # your code here
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod


def digits3(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    # your code here
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
