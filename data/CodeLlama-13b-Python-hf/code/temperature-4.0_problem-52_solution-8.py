def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in range(len(l) - 1, - 1, -1):
        if l[i] >= t:
            return False

    # return all(item < t in l)
    return l.count(num)

below_threshold()

