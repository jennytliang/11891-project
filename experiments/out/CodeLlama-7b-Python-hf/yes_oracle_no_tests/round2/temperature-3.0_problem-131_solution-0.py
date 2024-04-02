def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    # YOUR CODE HERE
    prod = 1
    if n == 0:
        return prod
    if n % 2 != 0:
        prod *= n
    while n > 0:
        r = n % 10
        if r % 2 != 0:
            prod *= r
        n //= 10
    return prod


print(digits(1))
print(digits(4))
print(digits(235))
