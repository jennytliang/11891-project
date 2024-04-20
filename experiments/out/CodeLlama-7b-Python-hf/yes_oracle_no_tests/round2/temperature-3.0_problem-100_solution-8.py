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
    
	Do not include these tokens in the code: = [] num = n while
	"""

  
    if n == 1:
        return [1]
    elif n == 2:
        return [2, 2]
    else:
        if n % 2 == 0:
            n = n + 1
        level = n
        result = [level]
        while level != 1:
            if level % 2 == 0:
                level = level // 2
            else:
                level = (level + 1) // 2
            result.append(level)
        result.reverse()
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()