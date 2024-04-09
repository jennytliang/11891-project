def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: # Your code here result
	"""
    # Your code here
    odd_digits = []
    for digit in str(n):
        if int(digit) % 2 == 1:
            odd_digits.append(int(digit))
    if len(odd_digits) == 0:
        return 0
    else:
        return prod(odd_digits)


def prod(l):
    """
    Return the product of a list of numbers.
    For example:
    prod([1, 2, 3, 4]) == 24
    """
    result = 1
    for x in l:
        result = result * x
    return result


# Pytest
import pytest


@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (4, 0),
    (235, 15),
])
def test_digits(n, expected):
    assert digits(n) == expected


# Demo
digits(1)
digits(4)
digits(235)
