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

    p = 1
    for i in str(n):
        if int(i) % 2 == 1:
            p *= int(i)

    return p


# tests
import pytest

from digits import digits

# test cases for digits
test_cases = [
    (123, 0),
    (1234, 0),
    (12345, 30),
    (123456789, 0),
    (1234567890, 90),
    (12345678901, 120),
    (123456789012, 240),
    (1234567890123, 360),
    (12345678901234, 480),
    (123456789012345, 600),
    (1234567890123456, 0),
    (12345678901234567, 720),
]

@pytest.mark.parametrize("n, expected", test_cases)
def test_digits(n, expected):
    assert digits(n) == expected


pytest.main()