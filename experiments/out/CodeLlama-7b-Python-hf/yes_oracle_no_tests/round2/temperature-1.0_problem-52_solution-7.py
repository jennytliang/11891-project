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
        else:
            return False


def sum_multiples(low: int, high: int, factors: list):
    """Return the sum of all the multiples of the given factors within the range low to high.
    >>> sum_multiples(1, 4, [2])
    6
    >>> sum_multiples(1, 10, [2, 3, 4])
    210
    >>> sum_multiples(1, 6, [4, 6])
    12
    """
    total = 0
    for i in range(low, high + 1):
        for x in factors:
            if i % x == 0:
                total += i
    return total


def count_multiples(low: int, high: int, factors: list):
    """Return the number of multiples of the given factors within the range low to high.
    >>> count_multiples(1, 4, [2])
    3
    >>> count_multiples(1, 10, [2, 3, 4])
    14
    >>> count_multiples(1, 6, [4, 6])
    3
    """
    count = 0
    for i in range(low, high + 1):
        for x in factors:
            if i % x == 0:
                count += 1
    return count


def sum_powers(n: int, p: int, limit: int):
    """Return the sum of the powers of n that are less than limit.
    >>> sum_powers(2, 3, 100)
    136
    >>> sum_powers(2, 4, 20)
    60
    >>> sum_powers(10, 6, 1000)
    30030
    """
    total = 0
    for x in range(1, limit):
        total += pow(n, p)
    return total


def count_divisible(low