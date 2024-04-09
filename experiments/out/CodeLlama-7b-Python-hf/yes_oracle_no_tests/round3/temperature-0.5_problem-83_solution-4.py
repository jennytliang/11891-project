def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    one_count = 0
    for i in range(10**(n-1), 10**n):
        if str(i).startswith('1') or str(i).endswith('1'):
            one_count += 1
    return one_count


def test_starts_one_ends():
    assert starts_one_ends(1) == 9
    assert starts_one_ends(2) == 90
    assert starts_one_ends(3) == 900


if __name__ == '__main__':
    test_starts_one_ends()
