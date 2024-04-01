def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    for i, elem in enumerate(l):
        l[i] = elem + i
    return l


if __name__ == '__main__':
    number = [1244, 432, 323, 52, 65535]
    for item in incr_list([6, 3, 2, 5]))