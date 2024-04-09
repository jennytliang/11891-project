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
    
	Include these tokens in the code: ans , num = [],
	Do not include these tokens in the code: # Write your code
	"""
    ans = []
    num = n
    while n >= 1:
        if n % 2 == 1:
            ans.append(num)
            num += 2
        else:
            ans.append(num)
            num += 4
        n -= 1
    return ans


def make_a_pile_in_one_line(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile_in_one_line(3)
    [3, 5, 7]
    
	Include these tokens in the code: ans , num = [],
	Do not include these tokens in the code: # Write your code
	"""
    return [n + 2 * i for i in range(n)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
