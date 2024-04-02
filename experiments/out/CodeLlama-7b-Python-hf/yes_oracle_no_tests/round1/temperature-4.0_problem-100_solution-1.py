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
        if i == 0:
            num.append(n)
        elif i == 1:
            num.append(num[0] + 2)
        else:
            if num[i-1] % 2 == 0:
                num.append(num[i-1] + 2)
            else:
                num.append(num[i-1] + 1)
    return num


def make_a_pile2(n):
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
        if i == 0:
            num.append(n)
        elif i == 1:
            num.append(num[0] + 2)
        else:
            num.append(num[i-1] + 2 - (num[i-1] % 2))
    return num


if __name__ == '__main__':
    import doctest
    doctest.testmod()
