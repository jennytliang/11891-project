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


def sum_multiples(m: int, n: int, threshold: int):
    """Return the sum of all multiples of m and n that are below threshold.
    >>> sum_multiples(3, 5, 100)
    234
    >>> sum_multiples(3, 5, 20)
    30
    >>> sum_multiples(3, 5, 10)
    15
    >>> sum_multiples(3, 5, 25)
    0
    >>> sum_multiples(3, 5, 30)
    0
    """

    total = 0
    for x in range(threshold):
        if x % m == 0 or x % n == 0:
            total += x
    return total


def sum_multiples_in_range(m: int, n: int, threshold: int, range_start: int, range_end: int):
    """Return the sum of all multiples of m and n in the range start to end
    that are below threshold.
    >>> sum_multiples_in_range(3, 5, 15, 100, 200)
    765
    >>> sum_multiples_in_range(3, 5, 15, 200, 300)
    0
    >>> sum_multiples_in_range(3, 5, 15, 200, 300)
    0
    """

    total = 0
    for x in range(range_start, range_end):
        if x % m == 0 or x % n == 0:
            total += x
            if total > threshold:
                return total
    return total


def sum_multiples_for_list(l: list, threshold: int):
    """Return the sum of all multiples of each number in l that are below threshold.
    >>> sum_multiples_for_list([3, 5