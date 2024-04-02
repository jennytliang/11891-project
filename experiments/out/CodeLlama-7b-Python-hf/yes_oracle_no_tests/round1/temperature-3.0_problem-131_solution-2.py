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
    # prod = 1
    # for i in range(10):
    #     if n % i == 0:
    #         prod *= i
    # return prod
    prod = 1
    while n > 0:
        if n % 2 == 1:
            prod *= n % 10
        n //= 10
    return prod
