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
    # pass
    prod = 1
    for i in range(len(str(n))):
        if int(str(n)[i]) % 2 == 1:
            prod *= int(str(n)[i])
    return prod


# print(digits(1))
# print(digits(4))
# print(digits(235))
