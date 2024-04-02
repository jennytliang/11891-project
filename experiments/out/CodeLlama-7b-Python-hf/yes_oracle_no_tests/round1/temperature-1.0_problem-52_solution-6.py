def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    pass


def sum_multiples(m: int, n: int, threshold: int):
    """Return the sum of multiples of m and n that are less than the threshold.
    >>> sum_multiples(3, 5, 100)
    23
    >>> sum_multiples(3, 5, 20)
    15
    """

    pass


def sum_multiples_below(m: int, n: int, threshold: int):
    """Return the sum of multiples of m and n that are less than the threshold.
    >>> sum_multiples_below(3, 5, 100)
    23
    >>> sum_multiples_below(3, 5, 20)
    15
    """
    s = 0
    i = 1
    while i < threshold:
        if i % m == 0 or i % n == 0:
            s += i
        i += 1
    return s


def sum_multiples_below2(m: int, n: int, threshold: int):
    """Return the sum of multiples of m and n that are less than the threshold.
    >>> sum_multiples_below2(3, 5, 100)
    23
    >>> sum_multiples_below2(3, 5, 20)
    15
    """
    s = 0
    i = 1
    while i < threshold:
        if i % m == 0 or i % n == 0:
            s += i
        i += 1
    return s


def sum_multiples_below3(m: int, n: int, threshold: int):
    """Return the sum of multiples of m and n that are less than the threshold.
    >>> sum_multiples_below3(3, 5, 100)
    23
    >>> sum_multiples_below3(3, 5, 20)
    15
    """
    s = 0
    i = 1
    while i < threshold: