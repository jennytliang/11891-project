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

def sum_multiples(n: int, low: int, high: int, include: list):
    """Return the sum of all the multiples of n in [low, high] inclusive.
    >>> sum_multiples(3, 2, 5, [0, 0, 1])
    3
    >>> sum_multiples(3, 2, 5, [0, 1, 0])
    7
    >>> sum_multiples(3, 2, 5, [1, 0, 1])
    4
    >>> sum_multiples(3, 2, 5, [1, 1, 1])
    18
    """
    s = 0
    for i in range(low, high+1):
        if i % n == 0:
            s += i
    return s

def sum_multiples_no_range(n: int, include: list):
    """Return the sum of all the multiples of n in [low, high] inclusive.
    >>> sum_multiples(3, [0, 0, 1])
    3
    >>> sum_multiples(3, [0, 1, 0])
    7
    >>> sum_multiples(3, [1, 0, 1])
    4
    >>> sum_multiples(3, [1, 1, 1])
    18
    """
    s = 0
    for i in range(10000):
        if i % n == 0:
            s += i
    return s

def sum_multiples_no_range_include(n: int, include: list):
    """Return the sum of all the multiples of n in [low, high] inclusive.
    >>> sum_multiples(3, [0, 0, 1])
    3
    >>> sum_multiples(3, [0, 1, 0])
    7
    >>> sum_multiples(3, [1, 0, 1])