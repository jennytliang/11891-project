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


def only_positive_numbers(l: list):
    """Return True if all numbers in the list l are positive.
    >>> only_positive_numbers([1, 3, 5, 7])
    True
    >>> only_positive_numbers([1, -3, 5, 7])
    False
    """
    for num in l:
        if num < 0:
            return False
    return True


def sum_of_items(l: list):
    """Return the sum of all numbers in the list l.
    >>> sum_of_items([1, 3, 5, 7])
    16
    """
    total = 0
    for num in l:
        total += num
    return total


def average(l: list):
    """Return the average of all numbers in the list l.
    >>> average([1, 3, 5, 7])
    4.0
    """
    total = 0
    for num in l:
        total += num
    return total / len(l)
