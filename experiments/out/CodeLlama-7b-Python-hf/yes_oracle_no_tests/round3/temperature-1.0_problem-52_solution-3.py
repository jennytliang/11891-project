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
    return False


def count_below_threshold(l: list, t: int):
    """Return the number of elements in the list l that are below threshold t.
    >>> count_below_threshold([1, 2, 4, 10], 100)
    4
    >>> count_below_threshold([1, 20, 4, 10], 5)
    2
    
	Include these tokens in the code: return 0
    """
    return 0


def sum_below_threshold(l: list, t: int):
    """Return the sum of elements in the list l that are below threshold t.
    >>> sum_below_threshold([1, 2, 4, 10], 100)
    11
    >>> sum_below_threshold([1, 20, 4, 10], 5)
    5
    
	Include these tokens in the code: return 0
    """
    return 0


def average_below_threshold(l: list, t: int):
    """Return the average of elements in the list l that are below threshold t.
    >>> average_below_threshold([1, 2, 4, 10], 100)
    2.75
    >>> average_below_threshold([1, 20, 4, 10], 5)
    2.5
    
	Include these tokens in the code: return 0
    """
    return 0


def sum_with_exception(l: list, t: int):
    """Return the sum of elements in the list l that are below threshold t.
    >>> sum_with_exception([1, 2, 4, 10], 100)
    11
    >>> sum_with_exception([1, 20, 4, 10], 5)
    5
    
	Include these tokens in the code: return 0
    """
    return 0


