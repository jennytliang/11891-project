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
        return 0
    prod = 1
    if n % 2 == 1:
        prod = prod * n
    while n > 0:
        n = n // 10
        if n % 2 == 1:
            prod = prod * (n % 10)
    return prod
