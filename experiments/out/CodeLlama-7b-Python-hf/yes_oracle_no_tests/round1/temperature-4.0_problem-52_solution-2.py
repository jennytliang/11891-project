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
    """Return the sum of all positive multiples of m and n that are below
    threshold.
    >>> sum_multiples(3, 5, 100)
    234
    
    Include these tokens in your code:
    + sum all multiples of m and n below threshold
    
    """

    total = 0
    i = m
    while i < threshold:
        total += i
        i += m
    i = n
    while i < threshold:
        total += i
        i += n
    return total
