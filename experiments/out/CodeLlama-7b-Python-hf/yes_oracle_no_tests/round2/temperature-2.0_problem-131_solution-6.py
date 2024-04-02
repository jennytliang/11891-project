def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: # code here
	"""
    # code here
    prod = 1
    for i in str(n):
        if int(i) % 2 == 1:
            prod *= int(i)
    return prod


def test_function():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(3000) == 0
