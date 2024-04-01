def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: p
	"""
    #code here
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod = prod * int(digit)
    return prod