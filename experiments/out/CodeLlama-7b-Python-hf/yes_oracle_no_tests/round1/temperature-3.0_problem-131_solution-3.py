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
    odd = False
    prod = 1
    while n > 0:
        if n % 2 == 1:
            odd = True
            prod *= n % 10
        n = n // 10
    return prod if odd else 0


def digits2(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = 1 ,
	"""
    # YOUR CODE HERE
    odd = False
    prod = 1
    while n > 0:
        if n % 2 == 1:
            odd = True
            prod *= n % 10
        n = n // 10
    return prod if odd else 0


def digits3(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = 1 ,
	"""
    # YOUR CODE HERE
    odd = False
    prod = 1
    while n > 0:
        if n % 2 == 1:
            odd = True
            prod *= n % 10
        n = n // 10
    return prod if odd else 0


def digits4(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has