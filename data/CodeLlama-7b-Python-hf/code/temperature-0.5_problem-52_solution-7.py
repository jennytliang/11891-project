def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for num in l:
        if num >= t:
            return False
    return True


def only_odd_numbers(l: list):
    """Return True if all numbers in the list l are odd.
    >>> only_odd_numbers([1, 3, 5, 7])
    True
    >>> only_odd_numbers([1, 2, 4, 10])
    False
    """
    for num in l:
        if num % 2 == 0:
            return False
    return True
