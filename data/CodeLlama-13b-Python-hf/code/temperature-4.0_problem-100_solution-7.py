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
    current = n
    stones = []
    while current > 0:
        stones.append(current)
        if current % 2 == 1:
            current -= 3
        elif current % 2 == 0:
            current -= 4
    return stones


if __name__ == "__main__":

    # print(list(enumerate(lst, start=1)))
