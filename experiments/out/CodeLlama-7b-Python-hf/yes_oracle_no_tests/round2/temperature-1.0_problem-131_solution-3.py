def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: # Your code here if
	"""
    # Your code here
    s = str(n)
    prod = 1
    for ch in s:
        if int(ch) % 2 == 1:
            prod *= int(ch)
    return prod


# Pybites solution


def digits1(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: # Your code here if
	"""
    # Your code here
    prod = 1
    for ch in str(n):
        if int(ch) % 2 == 1:
            prod *= int(ch)
    return prod
