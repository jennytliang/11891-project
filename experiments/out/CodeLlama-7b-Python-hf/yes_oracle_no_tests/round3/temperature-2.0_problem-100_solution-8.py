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
	Do not include these tokens in the code: # 1 - Write an algorithm
	"""
    # 1 - Write an algorithm
    ans = []
    num = n
    while n > 0:
        if n % 2 == 0:
            ans.append(num - n + 1)
        else:
            ans.append(num - n + 2)
        n -= 1
    return ans


def make_a_pile_2(n):
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
	Do not include these tokens in the code: # 1 - Write an algorithm
	"""
    # 1 - Write an algorithm
    ans = []
    num = n
    while n > 0:
        if n % 2 == 0:
            ans.append(num - n + 1)
        else:
            ans.append(num - n + 2)
        n -= 1
    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()
