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
    for d in str(n):
        if int(d) % 2 == 1:
            p *= int(d)
    return p


# tests
import pytest

from digits import digits


@pytest.mark.parametrize("arg, expected", [
    (1, 1),
    (4, 0),
    (555, 155),
    (22222222, 0),
    (123456789, 1),
    (1234567890, 0),
    (1234567890123456789012345678901234567890123456789012345678901234567890, 0),
    (13579, 13579),
    (4321, 4321),
    (105, 5),
    (100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000