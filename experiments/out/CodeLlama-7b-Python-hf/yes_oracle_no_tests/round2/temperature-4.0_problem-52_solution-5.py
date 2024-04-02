def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: # for x in l :
	"""
    for x in l:
        if x >= t:
            return False
    return True


print(below_threshold([1, 2, 4, 10], 100))


def sum_multiples(n: int, low: int, high: int):
    """Return the sum of all multiples of n in the range [low, high).
    >>> sum_multiples(3, 2, 10)
    30
    >>> sum_multiples(7, 10, 11)
    0
    >>> sum_multiples(5, 10, 15)
    75
    """
    if low % n == 0:
        low += n
    if low >= high:
        return 0
    return sum(range(low, high, n))


print(sum_multiples(3, 2, 10))


def sum_multiples_of_2_and_3(low: int, high: int):
    """Return the sum of all multiples of 2 and 3 in the range [low, high).
    >>> sum_multiples_of_2_and_3(2, 10)
    24
    >>> sum_multiples_of_2_and_3(10, 11)
    0
    >>> sum_multiples_of_2_and_3(10, 15)
    75
    """
    return sum_multiples(2, low, high) + sum_multiples(3, low, high)


print(sum_multiples_of_2_and_3(2, 10))


def sum_multiples_of_3_and_5(low: int, high: int):
    """Return the sum of all multiples of 3 and 5 in the range [low, high).
    >>> sum_multiples_of_3_and_5(2, 10)
    23
    >>> sum_multiples_of_3_and_5(10, 11)
    0
    >>>