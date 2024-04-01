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
    
	Include these tokens in the code: ans ,
	Do not include these tokens in the code: r = []
	"""
    # code below has been provided by the course staff
    ans = [n]
    while len(ans) < n:
        n = n + 1 if n % 2 == 0 else n + 2
        ans.append(n)
    return ans


def make_a_pile_v2(n):
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
    
	Include these tokens in the code: ans ,
	Do not include these tokens in the code: r = []
	"""
    # code below has been provided by the course staff
    ans = [n]
    while len(ans) < n:
        n = n + 1 if n % 2 == 0 else n + 2
        ans.append(n)
    return ans


print(make_a_pile_v2(3))
