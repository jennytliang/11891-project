def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    for x in l:
        if x < t:
            return True
    return False


def sum_multiples(l: list, n: int):
    """Return the sum of all multiples of n in list l.
    >>> sum_multiples([1, 2, 3, 4, 5], 3)
    0
    >>> sum_multiples([1, 3, 4, 6, 7], 3)
    12
    >>> sum_multiples([1, 3, 4, 6, 7], 5)
    0
    >>> sum_multiples([1, 3, 4, 6, 7], 6)
    12
    >>> sum_multiples([1, 3, 4, 6, 7], 10)
    0
    """

    total = 0
    for x in l:
        if x % n == 0:
            total += x
    return total


def count_multiples(l: list, n: int):
    """Return the number of multiples of n in list l.
    >>> count_multiples([1, 2, 3, 4, 5], 3)
    0
    >>> count_multiples([1, 3, 4, 6, 7], 3)
    2
    >>> count_multiples([1, 3, 4, 6, 7], 5)
    0
    >>> count_multiples([1, 3, 4, 6, 7], 6)
    2
    >>> count_multiples([1, 3, 4, 6, 7], 10)
    0
    """

    count = 0
    for x in l:
        if x % n == 0:
            count += 1
    return count


def distinct_powers(l: list):
    """Return True if the l contains all distinct numbers in the set
    {1, pow(2, 0), pow(2, 1), pow(2, 2), ...,