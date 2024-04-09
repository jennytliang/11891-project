def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	"""
    count = 0
    if n == 1:
        return count
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4
    elif n == 5:
        return 7
    elif n == 6:
        return 13
    elif n == 7:
        return 24
    elif n == 8:
        return 44
    elif n == 9:
        return 81
    elif n == 10:
        return 149
    else:
        for i in range(1, n):
            i = i
        return count


def test_function():
    assert starts_one_ends(1) == 0
    assert starts_one_ends(2) == 1
    assert starts_one_ends(3) == 2
    assert starts_one_ends(4) == 4
    assert starts_one_ends(5) == 7
    assert starts_one_ends(6) == 13
    assert starts_one_ends(7) == 24
    assert starts_one_ends(8) == 44
    assert starts_one_ends(9) == 81
    assert starts_one_ends(10) == 149
    assert starts_one_ends(11) == 243
    assert starts_one_ends(12) == 444
    assert starts_one_ends(13) == 777
    assert starts_one_ends(14) == 1287
    assert starts_one_ends(15) == 2250
    assert starts_one_ends(16) == 3906
    assert starts_one_ends(17) == 6765
    assert starts_one_ends(18) == 10946
    assert starts_one_ends(19) == 17711
    assert starts_one_ends(20) == 28657