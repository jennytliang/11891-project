def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    for x in range(len(l)):
        if l[x] >= t:
            return False
    return True


def find_second(l: list):
    """Return index of second largest number in list l (Assume that there is only
    one largest number).

    >>> find_second([1, 2, 4, 4])
    2
    >>> find_second([1, 2, 3, 4]) is None
    True
    >>> find_second([1, 2, 3, 3])
    1
    >>> find_second([5, 3, 1, 4])
    3
    """
    second = None

    for x in range(len(l)):
        if l[x] > l[0]:
            second = x
            break

    for x in range(len(l)):
        if l[x] > l[second]:
            second = x
    return second


