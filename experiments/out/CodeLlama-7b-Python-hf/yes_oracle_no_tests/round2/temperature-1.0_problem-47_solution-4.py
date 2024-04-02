def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    n = len(l)
    if n % 2 == 1:
        return sorted(l)[n // 2]
    else:
        return mean(sorted(l)[n // 2 - 1:n // 2 + 1])

def mean(l):
    """Return mean of the elements of l.

    >>> mean([1, 2, 3, 4])
    2.5
    """
    return sum(l) / len(l)
