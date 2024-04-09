def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    pass


def test_suite_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(10) == 0
    assert digits(1111) == 1
    assert digits(2468) == 0
    assert digits(123456789) == 0
    assert digits(99) == 9
    assert digits(100) == 1
    assert digits(11) == 1
    assert digits(121) == 1
    assert digits(1221) == 2
    assert digits(12345) == 3
    assert digits(1234567890) == 0
    assert digits(123456789012345678901234567890) == 0
    assert digits(1234567890123456789012345678901234567890) == 0
    assert digits(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000