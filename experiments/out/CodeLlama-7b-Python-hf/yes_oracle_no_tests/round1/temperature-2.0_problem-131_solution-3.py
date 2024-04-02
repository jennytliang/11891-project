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
    # Your code here
    str_n = str(n)
    prod = 1
    for digit in str_n:
        if int(digit) % 2 != 0:
            prod = prod * int(digit)
    return prod


# tests
# print(digits(1))
# print(digits(4))
# print(digits(235))
print(digits(42))
