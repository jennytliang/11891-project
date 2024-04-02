def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: # your code here if
	"""
    # your code here
    product = 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            product *= i
    return product


def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
