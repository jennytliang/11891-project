def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    if n == 1:
        return 1
    else:
        return 9 * starts_one_ends(n - 1)


def test_starts_one_ends():
    assert starts_one_ends(1) == 9
    assert starts_one_ends(2) == 90
    assert starts_one_ends(3) == 900
    assert starts_one_ends(4) == 9000
