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
        return 1
    if n < 0:
        return 0

    if n % 2 == 0:
        return 0
    
    return n % 2


# TESTS
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
assert digits(100) == 0
assert digits(101010) == 0
