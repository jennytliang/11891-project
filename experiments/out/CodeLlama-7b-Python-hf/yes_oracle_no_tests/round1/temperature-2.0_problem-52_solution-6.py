def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t for x in l
	"""

    return all(x < t for x in l)


def only_evens(l: list):
    """Return a list with only the even elements of l.
    >>> only_evens([1, 2, 4, 10])
    [2, 4]
    >>> only_evens([1, 3, 5])
    []
    """

    return [x for x in l if x % 2 == 0]


def sum_mod_5(l: list):
    """Return the sum of all elements of l modulo 5.
    >>> sum_mod_5([3, 4, 1, 6, 2])
    4
    """

    return sum(x % 5 for x in l)


def prod_mod_7(l: list):
    """Return the product of all elements of l modulo 7.
    >>> prod_mod_7([4, 1, 6, 2])
    4
    """

    return reduce(lambda x, y: (x * y) % 7, l)


def count_divisible_by(l: list, divisor: int):
    """Return the number of elements of l divisible by a given divisor.
    >>> count_divisible_by([3, 6, 9, 12, 15], 3)
    2
    """

    return len([x for x in l if x % divisor == 0])


def sum_mod_10(l: list):
    """Return the sum of all elements of l modulo 10.
    >>> sum_mod_10([3, 4, 1, 6, 2])
    12
    """

    return sum(x % 10 for x in l)


def prod_mod_12(l: list):
    """Return the product of all elements of l modulo 12.
    >>> prod_mod_12([4, 1, 6, 2])
    12
    """

    return reduce