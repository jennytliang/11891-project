def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""

    # Find the number of n-digit positive integers that start with 1
    # The number of n-digit positive integers that start with 1 is
    # the same as the number of n-digit positive integers that end with 0
    # For example, 100 and 001 are both 3-digit positive integers that start
    # with 1.
    start_ones = int('1' + '0' * (n - 1))

    # Find the number of n-digit positive integers that end with 1
    # The number of n-digit positive integers that end with 1 is
    # the same as the number of n-digit positive integers that start with 0
    # For example, 100 and 001 are both 3-digit positive integers that end
    # with 1.
    end_ones = int('0' * (n - 1) + '1')

    return start_ones + end_ones


def test_start_ones():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 2
    assert starts_one_ends(3) == 3


def test_end_ones():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 2
    assert starts_one_ends(3) == 3


def test_both_ones():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 2
    assert starts_one_ends(3) == 3


def test_start_and_end_ones():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 2
    assert starts_one_ends(3) == 3


def test_start_and_end_zeros():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 2
    assert starts_one_ends(3) == 3


def test_start