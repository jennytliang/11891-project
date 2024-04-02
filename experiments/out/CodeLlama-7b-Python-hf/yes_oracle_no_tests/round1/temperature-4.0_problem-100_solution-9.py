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
    # Your code here
    ans = [n]
    num = n
    while num != 1:
        if num % 2 == 1:
            num = num + 1
        else:
            num = num + 2
        ans.append(num)
    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
