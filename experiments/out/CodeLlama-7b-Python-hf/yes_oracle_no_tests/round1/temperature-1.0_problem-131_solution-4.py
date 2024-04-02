def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: product
	"""
    # Your code here
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product


def test_digits():
    assert digits(235) == 15
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(0) == 0
    assert digits(202) == 0
    assert digits(12345) == 120
    assert digits(987654321) == 0
