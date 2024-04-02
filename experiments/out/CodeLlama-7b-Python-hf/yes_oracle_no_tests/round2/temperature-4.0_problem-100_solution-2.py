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
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # BEGIN PROBLEM 2
    if n % 2 == 0:
        n += 1
    lst = []
    for i in range(n):
        if i % 2 == 0:
            lst.append(i + 1)
        else:
            lst.append(i + 2)
    return lst
    # END PROBLEM 2


def sum_of_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the sum of the stones in each level in a list, where element at index
    i represents the sum of stones in the level (i+1).

    Examples:
    >>> sum_of_pile(3)
    [3, 6, 10]
    """
    # BEGIN PROBLEM 3
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [3]
    if n % 2 == 0:
        n += 1
    lst = []
    for i in range(n):
        if i % 2 == 0:
            lst.append((i + 1) * (i + 2) // 2)
        else:
            lst.append((i + 2) * (i + 3) // 2)
    return lst
    # END PROBLEM 3
