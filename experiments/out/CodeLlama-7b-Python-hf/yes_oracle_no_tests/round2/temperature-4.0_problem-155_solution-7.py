def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: , odd
	"""

    # ------------------------------------------------------------------
    # WRITE YOUR SOLUTION HERE:
    # ------------------------------------------------------------------
    even = 0
    odd = 0
    for number in str(num):
        if int(number) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# tests
import pytest

# from even_odd_count import even_odd_count


@pytest.mark.parametrize(
    "arg, expected",
    [
        (-12, (1, 1)),
        (123, (1, 2)),
        (1230, (2, 2)),
        (12300, (3, 3)),
        (1000, (1, 3)),
        (1230000, (3, 6)),
        (10000, (1, 4)),
        (100000000000000000000000000000000000000000000000000000000000000000000000000, (2, 20)),
    ],
)
def test_even_odd_count(arg, expected):
    result = even_odd_count(arg)
    assert result == expected
