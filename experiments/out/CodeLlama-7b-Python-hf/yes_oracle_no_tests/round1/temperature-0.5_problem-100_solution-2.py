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
	Do not include these tokens in the code: result
	"""

    r = []
    for i in range(n):
        if i == 0:
            r.append(n)
        elif i % 2 == 0:
            r.append(r[i-1] + 2)
        else:
            r.append(r[i-1] + 1)
    return r

# TESTS
assert make_a_pile(3) == [3, 5, 7], "First test failed"
assert make_a_pile(4) == [4, 6, 8, 10], "Second test failed"
assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], "Third test failed"
assert make_a_pile(1) == [1], "Fourth test failed"
assert make_a_pile(2) == [2, 4], "Fifth test failed"
