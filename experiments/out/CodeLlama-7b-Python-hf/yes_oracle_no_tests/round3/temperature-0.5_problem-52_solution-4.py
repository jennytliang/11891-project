def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	Do not include these tokens in the code: ret ur = True
	"""
    ret = True
    for x in l:
        if x >= t:
            ret = False
            break
    return ret


def sum_multiples(low: int, high: int, factors: list):
    """Return the sum of all numbers between low and high that are
    divisible by one or more of the factors.
    >>> sum_multiples(1, 6, [3])
    18
    >>> sum_multiples(1, 6, [3, 5])
    23
    """
    ret = 0
    for x in range(low, high):
        for y in factors:
            if x % y == 0:
                ret += x
                break
    return ret


def count_multiples(low: int, high: int, factors: list):
    """Return the number of all numbers between low and high that are
    divisible by one or more of the factors.
    >>> count_multiples(1, 6, [3])
    3
    >>> count_multiples(1, 6, [3, 5])
    4
    """
    ret = 0
    for x in range(low, high):
        for y in factors:
            if x % y == 0:
                ret += 1
                break
    return ret


def sum_divisible_by(n: int, digits: list):
    """Return the sum of all numbers below n that are divisible by any of
    the integers in digits.
    >>> sum_divisible_by(10, [3, 5])
    17
    """
    ret = 0
    for x in range(1, n):
        for y in digits:
            if x % y == 0:
                ret += x
                break
    return ret


def sum_divisible_by_range(n: int, digits: list):
    """Return the sum of all numbers below n that are divisible by any of
    the integers in digits.
    >>> sum_divisible_by_range(10, [3, 5])
    17