def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: # Your code here product
	"""
    # Your code here
    # prod = 1
    # for char in str(n):
    #     if int(char) % 2 == 1:
    #         prod *= int(char)
    # return prod
    return reduce(lambda x, y: x * y, [int(d) for d in str(n) if int(d) % 2 == 1], 1)
