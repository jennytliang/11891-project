def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t for x in l
	"""
    return all(x < t for x in l)


def sum_of_multiples(limit: int, factors: list):
    """Return the sum of all multiples of the given factors below limit.

    >>> sum_of_multiples(6, [3,5])
    8
    >>> sum_of_multiples(6, [3,5,7])
    18
    """
    return sum(x for x in range(limit) if any(x % y == 0 for y in factors))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
