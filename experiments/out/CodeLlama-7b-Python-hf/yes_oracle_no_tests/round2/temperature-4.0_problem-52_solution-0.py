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
    


def sum_multiples(start, stop, step):
    """Return the sum of all integers from start to stop, inclusive,
    that are multiples of step.
    >>> sum_multiples(1, 3, 1)
    4
    >>> sum_multiples(1, 3, 2)
    2
    """
    total = 0
    for i in range(start, stop+1):
        if i % step == 0:
            total += i
    return total


def count_multiples(start, stop, step):
    """Return the number of integers from start to stop, inclusive,
    that are multiples of step.
    >>> count_multiples(1, 3, 1)
    3
    >>> count_multiples(1, 3, 2)
    1
    """
    count = 0
    for i in range(start, stop+1):
        if i % step == 0:
            count += 1
    return count


def sum_multiples_outside(start, stop, start_outside, stop_outside):
    """Return the sum of all integers from start to stop, inclusive,
    that are not multiples of start_outside or stop_outside.
    >>> sum_multiples_outside(1, 20, 3, 13)
    231
    >>> sum_multiples_outside(1, 20, 13, 13)
    227
    >>> sum_multiples_outside(1, 20, 13, 12)
    224
    >>> sum_multiples_outside(1, 2, 3, 13)
    0
    """
    total = 0
    for i in range(start, stop+1):
        if i not in range(start_outside, stop_outside+1):
            total += i
    return total


def count_multiples_out