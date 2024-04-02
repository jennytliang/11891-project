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
    """Return the sum of all the multiples of n in l.
    >>> sum_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    30
    >>> sum_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    25
    >>> sum_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)
    35
    """
    total = 0
    for x in l:
        if x % n == 0:
            total += x
    return total


def sum_all(l: list):
    """Return the sum of all the numbers in l.
    >>> sum_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    55
    >>> sum_all([4, 6, 2, 3, 5])
    18
    >>> sum_all([1])
    1
    """
    total = 0
    for x in l:
        total += x
    return total


def sum_above_threshold(l: list, t: int):
    """Return the sum of all the numbers in l that are above threshold t.
    >>> sum_above_threshold([1, 2, 4, 10], 100)
    14
    >>> sum_above_threshold([1, 20, 4, 10], 5)
    25
    >>> sum_above_threshold([1, 20, 4, 10], 10)
    24
    """
    total = 0
    for x in l:
       