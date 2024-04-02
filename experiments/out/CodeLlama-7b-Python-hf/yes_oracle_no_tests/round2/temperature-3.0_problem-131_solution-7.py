def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: # Your code here #
	"""
    # Your code here
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= (n % 10)
        n //= 10
    return result


def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: # Your code here #
	"""
    # Your code here
    odd_product = 1
    even_product = 1
    while n > 0:
        if n % 2 == 1:
            odd_product *= (n % 10)
        else:
            even_product *= (n % 10)
        n //= 10
    return odd_product * even_product