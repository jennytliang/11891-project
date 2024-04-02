def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    if n < 0:
        return -1
    if n == 0:
        return 0
    odd_digits = []
    for i in range(0, len(str(n))):
        digit = int(str(n)[i])
        if digit % 2 == 1:
            odd_digits.append(digit)
    if len(odd_digits) == 0:
        return 0
    else:
        return reduce(lambda x, y: x*y, odd_digits)


def digits_pythonic(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    if n < 0:
        return -1
    if n == 0:
        return 0
    odd_digits = [int(d) for d in str(n) if int(d) % 2 == 1]
    if len(odd_digits) == 0:
        return 0
    else:
        return reduce(lambda x, y: x*y, odd_digits)


def digits_pythonic_2(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    if n < 0:
        return -1
    if n == 0:
        return 0
    odd_digits = [int(d) for d in str(n) if int(d) % 2 == 1]
    if len(odd_digits) == 0:
        return