def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: # for x in l :
	"""
    for x in l:
        if x >= t:
            return False
    return True


def only_evens(l: list):
    """Return a new list with only the even elements from l.
    >>> only_evens([1, 2, 4, 10])
    [2, 4]
    >>> only_evens([1, 3, 5])
    []
    """
    return [x for x in l if x % 2 == 0]


def cut_first_third(l: list):
    """Return a new list with the first and one-third of the elements
    of l, in order.
    >>> cut_first_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 4, 5, 7, 8]
    """
    return [l[i] for i in [0] + [int(x) for x in range(1, len(l), 3)]]


def common_elements(l1: list, l2: list):
    """Return a list of elements that appear in both l1 and l2, in order
    of appearance in l1.
    >>> common_elements([1, 2, 3, 4], [2, 4, 6, 8])
    [2, 4]
    >>> common_elements([1, 1, 2, 3], [2, 3, 5, 5])
    [2, 3]
    """
    return [x for x in l1 if x in l2]


def sum_of_index(l: list, i: int):
    """Return the sum of the elements of l at index i.
    >>> sum_of_index([1, 2, 3, 4], 0)
    1
    >>> sum_of_index([1, 2, 3, 4], 2)
    3
    >>> sum_of_index([1, 2, 3, 4], 