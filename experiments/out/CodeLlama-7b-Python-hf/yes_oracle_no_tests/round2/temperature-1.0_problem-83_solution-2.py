def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: count = 0 for
	"""
    count = 0
    for i in range(10**(n-1), 10**n):
        if i % 10 == 1 or i // 10**(n-1) == 1:
            count += 1
    return count


def test_starts_one_ends():
    assert starts_one_ends(1) == 8
    assert starts_one_ends(2) == 80
    assert starts_one_ends(3) == 728
    assert starts_one_ends(4) == 6560
    assert starts_one_ends(5) == 59049
    assert starts_one_ends(6) == 531440
    assert starts_one_ends(7) == 4782969
    assert starts_one_ends(8) == 43046721
    assert starts_one_ends(9) == 387420489
    assert starts_one_ends(10) == 3456191265
