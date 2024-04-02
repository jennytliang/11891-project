def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd
	Do not include these tokens in the code: pass # tests
	"""
    product = 1
    while n > 0:
        if (n%10)%2 == 1:
            product *= n%10
        n = n//10
    return product

print(digits(1))
print(digits(10))
print(digits(123456789))
