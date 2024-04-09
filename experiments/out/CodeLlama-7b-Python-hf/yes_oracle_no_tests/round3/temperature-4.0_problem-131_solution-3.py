def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    # Your code here
    prod = 1
    
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            prod *= digit
        n = n // 10
    
    return prod


print(digits(1))
print(digits(4))
print(digits(235))
