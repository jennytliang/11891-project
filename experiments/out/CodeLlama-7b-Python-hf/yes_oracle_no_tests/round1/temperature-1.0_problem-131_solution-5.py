def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: product
	"""
    #YOUR CODE HERE
    digits = str(n)
    prod = 1
    for i in range(len(digits)):
        if int(digits[i]) % 2 != 0:
            prod *= int(digits[i])
    return prod