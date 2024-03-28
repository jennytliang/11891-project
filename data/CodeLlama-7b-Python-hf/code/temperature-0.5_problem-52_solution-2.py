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


def largest_item(l: list):
    """Return the largest number in the list l.
    >>> largest_item([1, 3, 5, 7])
    7
    """
    largest = l[0]
    for num in l:
        if num > largest:
            largest = num
    return largest


def smallest_item(l: list):
    """Return the smallest number in the list l.
    >>> smallest_item([1, 3, 5, 7])
    1
    """
    smallest = l[0]
    for num in l:
        if num < smallest:
            smallest = num
    return smallest

