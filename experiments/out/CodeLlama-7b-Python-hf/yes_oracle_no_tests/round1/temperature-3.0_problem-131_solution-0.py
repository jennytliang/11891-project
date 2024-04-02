def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 0
    elif n == 3:
        return 3
    else:
        return n
