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
        raise ValueError("n must be a positive integer")

    result = 1
    for d in str(n):
        if int(d) % 2 == 1:
            result *= int(d)

    return result
