def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i >= t:
            return False
    return True


def all_above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> all_above_threshold([1, 2, 4, 10], 5)
    False
    >>> all_above_threshold([1, 20, 4, 10], 5)
    True
    """
    for i in l:
        if i <= t:
            return False
    return True


def any_above_threshold(l: list, t: int):
    """Return True if any number in the list l is above threshold t.
    >>> any_above_threshold([1, 2, 4, 10], 5)
    True
    >>> any_above_threshold([1, 20, 4, 10], 5)
    True
    >>> any_above_threshold([1, 2, 4, 10], 20)
    False
    """
    for i in l:
        if i > t:
            return True
    return False


def all_below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> all_below_threshold([1, 2, 4, 10], 100)
    True
    >>> all_below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i >= t:
            return False
    return True


def all_equal(l: list):
    """Return True if all numbers in the list l are equal.
    >>> all_equal([1, 1, 1, 1])
    True
    >>> all_equal([1, 2, 3, 4])
    False
    >>> all_equal([1, 1, 1, 1, 2])
    False
    """
    for i in l:
        if i != l[0]:
            return False
    return True


def run_tests():
    import doctest
    doctest.testmod(verbose=True)


def main():
    run_tests()


if __name__ == "__main__":
    main()