def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t for x in l
	"""
    return all (x < t for x in l)


def sum_multiples(n: int, low: int, high: int):
    """Return the sum of the multiples of n in the range [low, high].
    >>> sum_multiples(3, 2, 5)
    3
    >>> sum_multiples(7, 3, 10)
    21
    >>> sum_multiples(4, 10, 25)
    30
    >>> sum_multiples(4, 1, 2)
    0
    >>> sum_multiples(5, 21, 21)
    0
    """
    return sum(range(low, high, n))


def sum_divisible_by(n: int, digits: list):
    """Return the sum of the digits in the list that are multiples of n.
    >>> sum_divisible_by(3, [1, 2, 3, 4, 5, 6])
    9
    >>> sum_divisible_by(7, [1, 2, 3, 4, 5, 6, 7, 8])
    16
    >>> sum_divisible_by(3, [4, 6, 9])
    0
    >>> sum_divisible_by(10, [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    0
    """
    return sum_multiples(n, min(digits), max(digits))


def sum_divisible_by_two(digits: list):
    """Return the sum of the digits in the list that are evenly divisible by 2.
    >>> sum_divisible_by_two([1, 2, 3, 4, 5, 6])
    6
    >>> sum_divisible_by_two([4, 6, 9])
    4
    >>> sum_divisible_by_two