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
    # your code here
    if n == 0:
        return 0
    odd = 1
    for x in str(n):
        if int(x) % 2 == 1:
            odd *= int(x)
    return odd


print(digits(123))
print(digits(124))
print(digits(123456789))
print(digits(1234567890))
print(digits(12345678901234567890))
