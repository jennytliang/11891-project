def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x < t:
            return True
        else:
            return False

    # for i in l:
    #     if i < t:
    #         return True
    #     else:
    #         return False

    # if all(i < t for i in l):
    #     return True
    # else:
    #     return False

def count_below_threshold(l: list, t: int):
    """Return the number of items in the list l that are below threshold t.
    >>> count_below_threshold([1, 2, 4, 10], 100)
    4
    >>> count_below_threshold([1, 20, 4, 10], 5)
    2
    >>> count_below_threshold([1, 2, 4, 10], 10)
    4
    >>> count_below_threshold([1, 2, 4, 10], 5)
    2
    """
    counter = 0
    for i in l:
        if i < t:
            counter += 1
    return counter



def sum_below_threshold(l: list, t: int):
    """Return the sum of all items in the list l that are below threshold t.
    >>> sum_below_threshold([1, 2, 4, 10], 100)
    13
    >>> sum_below_threshold([1, 20, 4, 10], 5)
    6
    >>> sum_below_threshold([1, 2, 4, 10], 10)
    13
    >>> sum_below_threshold([1, 2, 4, 10], 5)
    6
    """
    counter = 0
    for i in l:
        if i < t:
            counter += i
    return counter


def count_string(l: list, s: str):
    """Return the number of times s appears in l.
    >>> count