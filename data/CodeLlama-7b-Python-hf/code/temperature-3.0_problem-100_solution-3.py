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
    """
    if n < 0:
        raise ValueError('must be positive integer')
    if n == 0:
        return []
    elif n == 1:
        raise ValueError('must be positive integer')
    elif n == 2:
        return [2, 4]
    elif n % 2 == 1:
        result = [n, (n+1)*2]
    elif n % 2 == 0:
        result = [n, (n+2)*2]
    return result


def test_L03P13_solutions():
    """Run the test functions.
    >>> test_L03P13_solutions()
    """
    import doctest
    doctest.run_docstring_examples(make_a_pile, locals(), verbose=True)
