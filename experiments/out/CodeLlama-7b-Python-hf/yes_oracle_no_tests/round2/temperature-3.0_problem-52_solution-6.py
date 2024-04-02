def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    # for x in l:
    #     if x >= t:
    #         return False
    # return True

    # return all(x < t for x in l)

    return not any(x >= t for x in l)


def only_evens(l: list):
    """Return a new list with only the even elements from l.
    >>> only_evens([1, 2, 4, 10, 6])
    [2, 4, 6]
    >>> only_evens([1, 3, 5])
    []
    """

    # return [x for x in l if x % 2 == 0]

    return list(filter(lambda x: x % 2 == 0, l))


def multiples_of_index(l: list):
    """Return a new list with the elements of l multiplied by the index. 
    The index is the position of the element in the list.
    >>> multiples_of_index([1, 2, 3, 4, 5])
    [1, 4, 9, 16, 25]
    >>> multiples_of_index([3, 4, 5, 6, 7])
    [0, 8, 18, 28, 38]
    """

    # return [x * (i + 1) for i, x in enumerate(l)]

    return list(map(lambda x: x * (i + 1), l))


def reverse_list(l: list):
    """Return a new list with the elements of l reversed.
    >>> reverse_list([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> reverse_list([1, 2, 3, 4, 5, 6])
    [6, 5, 4, 3, 2, 1]
    """

    # return l[::-1]

    return list(reversed(l))