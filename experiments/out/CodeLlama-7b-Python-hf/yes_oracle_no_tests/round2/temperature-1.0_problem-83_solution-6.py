def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # set up a counter
    counter = 0
    # loop through the numbers
    for num in range(10**(n-1), 10**n):
        # increment the counter if the number starts or ends with 1
        if str(num)[0] == '1' or str(num)[-1] == '1':
            counter += 1
    # return the counter
    return counter


# tests
import pytest

# expected output
# starts_one_ends(2) -> 3
# starts_one_ends(3) -> 4
# starts_one_ends(4) -> 5
# starts_one_ends(5) -> 6
# starts_one_ends(6) -> 7
# starts_one_ends(7) -> 8
# starts_one_ends(8) -> 9
# starts_one_ends(9) -> 10
# starts_one_ends(10) -> 11

# tests
from random import randint


@pytest.mark.parametrize('n', [randint(2, 10)])
def test_starts_one_ends(n, solutions):
    assert solutions.starts_one_ends(n) == starts_one_ends(n)


def test_starts_one_ends_error():
    with pytest.raises(TypeError):
        starts_one_ends('1')
