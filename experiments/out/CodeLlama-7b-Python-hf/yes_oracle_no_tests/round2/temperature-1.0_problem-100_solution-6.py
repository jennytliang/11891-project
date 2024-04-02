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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: # Create an empty list
	"""
    ans = []
    if n > 0:
        ans.insert(0, n)
        for i in range(1, n):
            if (i+1) % 2 != 0:
                ans.insert(0, ans[0]+(i+1))
            else:
                ans.insert(0,ans[0]+(i+2))
    return ans
