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

    return all(x < t for x in l)


def count_below_threshold(l: list, t: int):
    """Return the number of elements in l that are below threshold t.
    >>> count_below_threshold([1, 2, 4, 10], 100)
    4
    >>> count_below_threshold([1, 20, 4, 10], 5)
    3
    
	Include these tokens in the code: return the number of times ( x < t
	"""

    # return sum(1 for x in l if x < t)

    return sum(x < t for x in l)


def large_diff(l: list):
    """Returns True if the maximum element is within 10 of the minimum element.
    >>> large_diff([10, 4, 2, 1])
    False
    >>> large_diff([1000, 999, 998])
    True
    
	Include these tokens in the code: return True if max - min < 10
	"""

    # return max(l) - min(l) < 10

    return max(l) - min(l) <= 10


def small_diff(l: list):
    """Returns True if the maximum element is within 10 of the minimum element.
    >>> small_diff([10, 4, 2, 1])
    True
    >>> small_diff([1000, 999, 998])
    False
    
	Include these tokens in the code: return True if max - min > 10
	"""

    # return max(l) - min(l) > 10

    return max(l) - min(l) >= 10


def same_first_and_last(l: list):
    """Return True if the first element in the list is the same