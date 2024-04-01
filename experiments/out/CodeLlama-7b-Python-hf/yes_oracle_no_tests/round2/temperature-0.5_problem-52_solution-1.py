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
    """Return the sum of all the multiples of n in l.
    >>> sum_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    30
    >>> sum_multiples([1, 1, 1, 1, 1, 1, 1, 1], 7)
    0
    >>> sum_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    45
    >>> sum_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    54
    """
    return sum(x for x in l if x % n == 0)

def product_of_all_but_one(l: list):
    """Return the product of all the numbers in l except for the
    last one.
    >>> product_of_all_but_one([1, 2, 3, 4])
    24
    >>> product_of_all_but_one([1, 2])
    2
    >>> product_of_all_but_one([-12, 12, 0, 2])
    0
    >>> product_of_all_but_one([])
    Traceback (most recent call last):
        ...
    ValueError: list must have at least 1 element
    """
    if len(l) == 0:
        raise ValueError('list must have at least 1 element')
    return 1 if len(l) == 1 else reduce(lambda x, y: x * y, l[:-1])


def contains_sublist(l1: list, l2: list):
    """Returns True if l2 appears in l1.
    >>> contains_sublist([1, 2, 3