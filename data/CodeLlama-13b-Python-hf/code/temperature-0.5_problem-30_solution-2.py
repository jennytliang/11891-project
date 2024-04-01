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
    [-5, -3, -10]
    """
    return [x for x in l if x < 0]


def get_even(l: list):
    """Return only even numbers in the list.
    >>> get_even([-1, 2, -4, 5, 6])
    [2, 6]
    >>> get_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [2, 0, -2]
    """
    return [x for x in l if x % 2 == 0]


def get_odd(l: list):
    """Return only odd numbers in the list.
    >>> get_odd([-1, 2, -4, 5, 6])
    [-1, -4, 5]
    >>> get_odd([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, 3, 9, 1, -10]
    """
    return [x for x in l if x % 2 != 0]


def get_divisible_by(l: list, n: int):
    """Return only numbers divisible by n in the list.
    >>> get_divisible_by([-1, 2, -4, 5, 6], 2)
    [-4, 2, 6]
    >>> get_divisible_by([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 3)
    [3, -3, 9, -10]
    """
    return [x for x in l if x % n == 0]


def get_not_divisible_by(l: list, n: int):
    """Return only numbers not divisible by n in the list.
    >>> get_not_divisible_by([-1, 2, -4, 5, 6], 2)
    [-1, 5]
    >>> get_not_divisible_by([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 3)
    [-5, 2, 0, 1]
    """
    return [x for x in l if x % n != 0]
