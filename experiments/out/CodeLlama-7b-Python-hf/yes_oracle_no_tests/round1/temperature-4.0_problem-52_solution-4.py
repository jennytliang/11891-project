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


def sum_multiples(n: int, low: int, high: int):
    """Return the sum of integers from low to high that are multiples of n.
    >>> sum_multiples(3, 2, 5)
    3
    >>> sum_multiples(5, 2, 5)
    0
    >>> sum_multiples(0, 2, 5)
    0
    >>> sum_multiples(3, 2, 4)
    3
    >>> sum_multiples(3, 2, 10)
    9
    >>> sum_multiples(3, 2, 2)
    0
    >>> sum_multiples(3, 3, 5)
    0
    
    Modify the code so that it returns 0 if low is not a multiple of n.
    Modify the code so that it returns 0 if low > high.
    Modify the code so that it returns 0 if n = 0.
    """
    if low % n == 0:
        return sum([x for x in range(low, high+1, n)])
    else:
        return 0


def sum_divisible(n: int, high: int):
    """Return the sum of all positive integers up to and including high
    that are divisible by n.
    >>> sum_divisible(3, 9)
    18
    >>> sum_divisible(5, 10)
    45
    >>> sum_divisible(1, 10)
    55
    >>> sum_divisible(1, 11)
    55
    >>> sum_divisible(7, 11)
    55
    >>> sum_divisible(11, 11)
    0
    >>> sum_divisible(11, 10)
    0
    >>> sum_divisible(2, 2)
    2
    >>> sum_divisible(3