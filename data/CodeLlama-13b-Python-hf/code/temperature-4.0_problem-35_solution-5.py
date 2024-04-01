def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # return  l[len(l) - max_index(l, 1)]
    return max(l) if l else -float('inf')


def is_sorted(l:  list):
    """Returns whether the list l is sorted. If yes returns True,
    in other case returns False.
