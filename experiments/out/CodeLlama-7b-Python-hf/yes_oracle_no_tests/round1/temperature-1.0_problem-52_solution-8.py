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



def sum_multiples(low: int, high: int, factors: list):
    """Return the sum of all the multiples of the given list of factors between
    the low and high limits.
    >>> sum_multiples(1, 5, [3, 5])
    30
    >>> sum_multiples(1, 6, [3, 5])
    33
    >>> sum_multiples(1, 6, [3, 7])
    0
    """

    return sum([x for x in range(low, high) if all(x % y == 0 for y in factors)])

def sum_multiples_II(low: int, high: int, factors: list):
    """Return the sum of all the multiples of the given list of factors between
    the low and high limits.
    >>> sum_multiples(1, 5, [3, 5])
    30
    >>> sum_multiples(1, 6, [3, 5])
    33
    >>> sum_multiples(1, 6, [3, 7])
    0
    """

    # sum([x for x in range(low, high) if all(x % y == 0 for y in factors)])
    return sum([x for x in range(low, high) if any(x % y == 0 for y in factors)])



def count_conditional_II(cond: bool, a: list):
    """Return the number of elements in list a for which the condition cond is
    true.
    >>> count_conditional_II(lambda x: x % 2 == 0, [1, 2, 3, 4])
    2
    >>> count_conditional_II(lambda x: x > 3, [1, 2, 3, 4])
    2
    >>> count_conditional_II(lambda x: x < 3, [1, 2, 3, 4])
    2
    """

