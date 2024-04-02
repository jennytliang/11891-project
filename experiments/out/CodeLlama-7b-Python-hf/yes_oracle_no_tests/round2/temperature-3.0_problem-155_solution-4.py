def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    for i in range(num):
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even, odd


# tests
import pytest

from even_odd_count import even_odd_count

@pytest.mark.parametrize("num, expected", [
    (1, (0, 1)),
    (12, (1, 1)),
    (-123, (1, 2)),
    (12345678, (4, 4)),
    (111111111111111111111111111111111111111111111111111111111111111111111111111111111, (1, 63)),
    (1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111