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
	Do not include these tokens in the code: r _ list = []
	"""
    ans = []
    i = n
    while i >= 0:
        if i % 2 == 0:
            ans.append(i+1)
        else:
            ans.append(i+2)
        i -= 1
    return ans
