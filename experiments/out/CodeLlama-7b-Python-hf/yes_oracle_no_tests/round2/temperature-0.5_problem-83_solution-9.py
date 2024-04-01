def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""

    # The number of numbers that start or end with 1 is the same as the number of numbers that start or end with 9
    # because it is the same as the number of numbers that start or end with any other digit.
    # The number of numbers that start or end with 1 is the same as the number of numbers with 1 as the middle digit.
    # The number of numbers with 1 as the middle digit is the same as the number of numbers with 1 as the leading digit.
    # The number of numbers with 1 as the leading digit is the same as the number of numbers with 1 as the trailing digit.
    # The number of numbers with 1 as the trailing digit is n - 2.

    return (n - 2) * 4


def test_starts_one_ends():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 3
    assert starts_one_ends(3) == 7
    assert starts_one_ends(4) == 13
    assert starts_one_ends(5) == 24
    assert starts_one_ends(6) == 43
    assert starts_one_ends(7) == 77
    assert starts_one_ends(8) == 136
    assert starts_one_ends(9) == 243
    assert starts_one_ends(10) == 444


if __name__ == '__main__':
    test_starts_one_ends()
