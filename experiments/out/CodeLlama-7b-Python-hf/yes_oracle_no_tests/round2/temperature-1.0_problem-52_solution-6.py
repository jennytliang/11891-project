def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t for x in l
	"""
    return all(x < t for x in l)


def sum_multiples(l: list, n: int):
    """Return the sum of all the elements of l that are multiples of n.
    >>> sum_multiples([2, 3, 4, 5, 6, 7], 3)
    3
    >>> sum_multiples([2, 3, 4, 5, 6, 7], 5)
    7
    >>> sum_multiples([2, 3, 4, 5, 6, 7], 7)
    0
    """
    return sum(x for x in l if x % n == 0)


def count_multiples(l: list, n: int):
    """Return the number of elements of l that are multiples of n.
    >>> count_multiples([2, 3, 4, 5, 6, 7], 3)
    2
    >>> count_multiples([2, 3, 4, 5, 6, 7], 5)
    1
    >>> count_multiples([2, 3, 4, 5, 6, 7], 7)
    0
    """
    return len([x for x in l if x % n == 0])


def sum_divisors(n: int):
    """Return the sum of all positive divisors of n, not including n.
    >>> sum_divisors(20)
    81
    >>> sum_divisors(28)
    165
    >>> sum_divisors(14)
    42
    """
    return sum(x for x in range(1, n) if n % x == 0)


def count_divisors(n: int):
    """Return the number of positive divisors of n, not including n.
    >>> count_divisors(20)
    4
    >>> count_divisors(28)
    6
    >>> count_divisors(14)
    3
    """
    return len