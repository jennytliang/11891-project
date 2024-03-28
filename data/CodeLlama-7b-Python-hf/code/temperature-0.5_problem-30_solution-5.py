def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]


def get_negative(l: list):
    """Return only negative numbers in the list.
    >>> get_negative([-1, 2, -4, 5, 6])
    [-1, -4]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-10]
    """
    return [x for x in l if x < 0]


def get_non_negative(l: list):
    """Return only non-negative numbers in the list.
    >>> get_non_negative([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_non_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 0, 123, 1]
    """
    return [x for x in l if x >= 0]


def get_non_positive(l: list):
    """Return only non-positive numbers in the list.
    >>> get_non_positive([-1, 2, -4, 5, 6])
    [-1, -4]
    >>> get_non_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-10]
    """
    return [x for x in l if x <= 0]


def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, -4, 5, 6])
    [-1, 5]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-1, 5, 3, 9, -3]
    """
    return [x for x in l if x % 2 != 0]


def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([-1, 2, -4, 5, 6])
    [2, -4, 6]
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, -3, 3, 0, 123]
    """
    return [x for x in l if x % 2 == 0]


def get_divisible_by_n(l: list, n: int):
    """Return only numbers divisible by n in the list.
    >>> get_divisible_by_n([-1, 2, -4, 5, 6], 2)
    [2, -4, 6]
    >>> get_divisible_by_n([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 3)
    [3, 9, -3]
    """
    return [x for x in l if x % n == 0]


def get_not_divisible_by_n(l: list, n: int):
    """Return only numbers not divisible by n in the list.
    >>> get_not_divisible_by_n([-1, 2, -4, 5, 6], 2)
    [-1, 5]
    >>> get_not_divisible_by_n([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 3)
    [-1, 2, -4, 6]
    """
    return