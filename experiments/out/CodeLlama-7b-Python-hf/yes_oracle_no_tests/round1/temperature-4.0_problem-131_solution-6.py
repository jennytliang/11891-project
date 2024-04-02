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
    n_string = str(n)
    prod = 1
    for i in n_string:
        if int(i) % 2 == 1:
            prod *= int(i)
        else:
            continue
    return prod


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
    n_string = str(n)
    prod = 1
    for i in n_string:
        if int(i) % 2 == 1:
            prod *= int(i)
        else:
            continue
    return prod


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
    n_string = str(n)
    prod = 1
    for i in n_string:
        if int(i) % 2 == 1:
            prod *= int(i)
        else:
            continue
    return prod


def digits4(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = 1 ,
	"""