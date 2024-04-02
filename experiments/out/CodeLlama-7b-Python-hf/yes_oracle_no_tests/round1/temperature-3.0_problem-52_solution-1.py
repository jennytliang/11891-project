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


def first_is_not(l: list, x: int):
    """Return True if the first element in the list l is not x.
    >>> first_is_not([1, 2, 4, 10], 100)
    True
    >>> first_is_not([100, 20, 4, 10], 100)
    False
    
	Include these tokens in the code: return not l[0] == x
	"""
    return not l[0] == x


def all_above_average(l: list):
    """Return True if all the numbers in the list l are above the average of l.
    >>> all_above_average([1, 3, 5, 7])
    True
    >>> all_above_average([1, 3, 2, 7])
    False
    
	Include these tokens in the code: return all( x > average(l)
	"""
    average = sum(l) / len(l)
    return all(x > average for x in l)


def max_is_not(l: list, x: int):
    """Return True if the maximum value in l is not x.
    >>> max_is_not([1, 3, 5, 7], 7)
    False
    >>> max_is_not([1, 3, 5, 7], 5)
    True
    
	Include these tokens in the code: return max(l) != x
	"""
    return max(l) != x


def above_average(l: list):
    """Return the elements in l that are above the average of l.
    >>> above_average([1, 3, 5, 7])
    [5, 7]
    >>> above_average([3, 3, 5, 7])
    [5, 7]
    
	Include these tokens in the code: return [x for x in l