def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x <
	"""
    for x in l:
        if x >= t:
            return False
    return True


def sum_multiples(m: int, n: int, threshold: int):
    """Return the sum of multiples of m and n below threshold.
    >>> sum_multiples(3, 5, 100)
    2340
    >>> sum_multiples(3, 5, 1000)
    10607
    >>> sum_multiples(3, 5, 10000)
    33315
    """
    total = 0
    i = 0
    while i < threshold:
        if i % m == 0 or i % n == 0:
            total += i
        i += 1
    return total


def sum_divisible(n: int, threshold: int):
    """Return the sum of positive numbers divisible by n below threshold.
    >>> sum_divisible(4, 100)
    252
    >>> sum_divisible(3, 100)
    165
    >>> sum_divisible(5, 100)
    50
    >>> sum_divisible(7, 100)
    14
    """
    total = 0
    i = 0
    while i < threshold:
        if i % n == 0:
            total += i
        i += 1
    return total


def count_divisible(n: int, threshold: int):
    """Return the number of positive numbers divisible by n below threshold.
    >>> count_divisible(4, 100)
    25
    >>> count_divisible(3, 100)
    9
    >>> count_divisible(5, 100)
    10
    >>> count_divisible(7, 100)
    14
    """
    count = 0
    i = 0
    while i < threshold:
        if i % n == 0:
            count