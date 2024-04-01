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
    result = []
    if n % 2 == 1:
        result.append(n)
    elif n % 2 == 0:
        result.append(n+1)

    # add the rest
    while n != 1 and n % 2 == 1:
        n += 3

    if n != 1:
        result += [i + 2 for i in range(0, n//2 - 2)]
    if 2 * (n//2 - 1) == n:
        result += [n]

    # 5  # 4 3  # 3 2 # 2 1
    # 4 1  # 3 0 # 2  # 1

        # n = n + 1
    print(result.pop(-1), result)
