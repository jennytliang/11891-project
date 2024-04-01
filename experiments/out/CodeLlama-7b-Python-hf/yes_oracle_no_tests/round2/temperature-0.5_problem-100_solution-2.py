def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    
	Include these tokens in the code: ans , num
	Do not include these tokens in the code: r
	"""
    ans = []
    num = n
    while num != 0:
        if num % 2 == 0:
            num += 1
        ans.append(num)
        num += 2
    return ans


def make_a_pile_pythonic(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    
	Include these tokens in the code: ans , num
	Do not include these tokens in the code: r
	"""
    ans = []
    num = n
    while num != 0:
        ans.append(num)
        num += 2 if num % 2 == 0 else 1
    return ans


def run_test(test_cases=None):
    test_cases = test_cases or [
        # (argument, expected_result)
        (3, [3, 5, 7]),
        (4, [4, 6, 8, 10]),
        (5, [5, 7, 9, 11, 13]),
    ]
    for arg, expected in test_cases:
        assert make_a_pile(arg) == expected
        assert make_a_pile_pythonic(arg) == expected


if __name__ == "__main__":
    import doctest

    doctest.testmod()
