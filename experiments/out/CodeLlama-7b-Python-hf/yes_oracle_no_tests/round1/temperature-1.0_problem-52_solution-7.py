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


def sum_multiples(l: list, n: int):
    """Return the sum of all the elements of l that are multiples of n.
    >>> sum_multiples([2, 4, 5, 10, 11, 12], 3)
    18
    >>> sum_multiples([2, 4, 5, 10, 11, 12], 5)
    20
    
	Include these tokens in the code: for x in l: if x % n == 0: return x + ...
    """
    total = 0
    for x in l:
        if x % n == 0:
            total += x
    return total
