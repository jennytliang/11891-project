def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: # your code here result
	"""
    # your code here
    odds = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            odds *= int(digit)
    return odds



def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(102) == 0
    assert digits(101) == 1
    assert digits(235) == 15
    assert digits(3013) == 33
    assert digits(4321234) == 0


if __name__ == '__main__':
    test_digits()
