def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x >= t:
            return False
    return True


def all_same_sign(l: list):
    """Return True if all numbers in the list l have the same sign.
    >>> all_same_sign([1, 2, 4, 10])
    True
    >>> all_same_sign([1, -2, 4, 10])
    False
    """
    return all(x >= 0 for x in l) or all(x < 0 for x in l)


def all_below_avg(l: list, a: int):
    """Return True if all numbers in the list l are below their average.
    >>> all_below_avg([1, 2, 3], 2)
    True
    >>> all_below_avg([1, 2, 3], 0)
    False
    """
    return below_threshold(l, avg(l))


def avg(l: list):
    """Return the average of the numbers in list l.
    >>> avg([10, 40, 60])
    40.0
    """
    return sum(l) / len(l)


def max_val(l: list):
    """Return the maximum value from the given list.
    >>> max_val([10, 40, 60])
    60
    """
    return max(l)


def min_val(l: list):
    """Return the minimum value from the given list.
    >>> min_val([10, 40, 60])
    10
    """
    return min(l)


def above_average(l: list):
    """Return a list of the values from l that are above average.
    >>> above_average([10, 40, 60])
    [40, 60]
    """
    return [x for x in l if x > avg(l)]


def below_average(l: list):
    """Return