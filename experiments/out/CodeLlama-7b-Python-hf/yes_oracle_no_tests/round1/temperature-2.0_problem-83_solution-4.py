def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: result = 0 for
	"""
    num_ones = 10 ** (n - 1)
    num_twos = 10 ** n - num_ones
    return (num_ones - 1) * (num_twos - 1)


# Pytest
def test_starts_one_ends():
    assert starts_one_ends(1) == 9
    assert starts_one_ends(2) == 45
    assert starts_one_ends(3) == 354
    assert starts_one_ends(4) == 3083
    assert starts_one_ends(5) == 2744
    assert starts_one_ends(6) == 2504
    assert starts_one_ends(7) == 2320
    assert starts_one_ends(8) == 2140
    assert starts_one_ends(9) == 2004
    assert starts_one_ends(10) == 1890
