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
    
	Include these tokens in the code: ans , num = [], n
	"""
    ans = []
    num = []
    for i in range(n):
        num.append(i+1)
    for i in range(n):
        if i % 2 == 0:
            ans.append(num[i] + num[i + 1])
        else:
            ans.append(num[i] + num[i + 1] + 1)
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
    The solution must be recursive.

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    
	Include these tokens in the code: ans , num = [], n
	"""
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,3]
    elif n % 2 == 0:
        return [n] + make_a_pile_2(n-2) + [n+2]
    else:
        return [n] + make_a_pile_2(n-1) + [n+1]
