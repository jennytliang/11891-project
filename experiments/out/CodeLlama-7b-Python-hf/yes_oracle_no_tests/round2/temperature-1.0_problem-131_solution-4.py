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
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    if n % 2 == 1:
        product = 1
        while n > 0:
            product = product * n
            n = n // 10
        return product


print(digits(1))
print(digits(4))
print(digits(235))
