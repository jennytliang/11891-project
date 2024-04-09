def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: # your code here product
	"""
    # your code here
    prod = 1
    for i in str(n):
        if int(i) % 2 == 1:
            prod *= int(i)
    return prod


print(digits(12345))
print(digits(123456))
print(digits(123))
print(digits(123456789))

# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 3
# 1 3 5 7 9
