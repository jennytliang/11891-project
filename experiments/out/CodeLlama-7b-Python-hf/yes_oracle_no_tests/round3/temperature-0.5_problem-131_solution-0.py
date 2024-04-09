def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    odd_digits = []
    for digit in str(n):
        if int(digit) % 2 != 0:
            odd_digits.append(int(digit))
    if len(odd_digits) == 0:
        return 0
    else:
        return reduce(lambda x, y: x * y, odd_digits)


def digits2(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    return reduce(lambda x, y: x * y, [int(digit) for digit in str(n) if int(digit) % 2 != 0])
