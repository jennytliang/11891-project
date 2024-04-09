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


def sum_multiples(n: int, low: int, high: int):
    """Return the sum of all the multiples of n in the range [low, high].
    >>> sum_multiples(3, 2, 5)
    3
    >>> sum_multiples(5, 1, 100)
    2310
    >>> sum_multiples(7, 100, 200)
    1429
    >>> sum_multiples(11, 900, 1000)
    0
    """
    sum_multiples = 0
    for i in range(low, high):
        if i % n == 0:
            sum_multiples += i
    return sum_multiples


def count_multiples(n: int, low: int, high: int):
    """Return the number of multiples of n in the range [low, high].
    >>> count_multiples(2, 2, 5)
    3
    >>> count_multiples(3, 1, 100)
    23
    >>> count_multiples(7, 100, 200)
    14
    >>> count_multiples(11, 900, 1000)
    0
    """
    count = 0
    for i in range(low, high):
        if i % n == 0:
            count += 1
    return count


def sum_divisible_by(n: int, low: int, high: int):
    """Return the sum of all numbers divisible by n in [low, high].
    >>> sum_divisible_by(3, 1, 5)
    0
    >>> sum_divisible_by(3, 1, 6)
    3
    >>> sum_divisible_by(3, 1, 7)
    3
    >>> sum_divisible_by(3, 5,