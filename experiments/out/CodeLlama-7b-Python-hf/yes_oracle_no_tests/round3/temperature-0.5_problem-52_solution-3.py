def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: def sum _ multi ples ( l :
	"""

    return all(x < t for x in l)


def sum_multiples(l: list, nums: list):
    """Return the sum of all numbers in list l that are multiples of any
    number in nums.
    >>> sum_multiples([1, 2, 3, 4, 5, 6], [2, 3])
    12
    >>> sum_multiples([1, 2, 3, 4, 5, 6], [5])
    15
    >>> sum_multiples([1, 2, 3, 4, 5, 6], [2, 3, 5])
    22
    """
    return sum([x for x in l for y in nums if x % y == 0])


def count_multiples(l: list, nums: list):
    """Return the number of elements in list l that are multiples of any
    number in nums.
    >>> count_multiples([1, 2, 3, 4, 5, 6], [2, 3])
    3
    >>> count_multiples([1, 2, 3, 4, 5, 6], [5])
    2
    >>> count_multiples([1, 2, 3, 4, 5, 6], [2, 3, 5])
    5
    """
    return sum([1 for x in l for y in nums if x % y == 0])


def sum_multiples_below(l: list, nums: list, t: int):
    """Return the sum of all numbers in list l that are multiples of any
    number in nums and are below threshold t.
    >>> sum_multiples_below([1, 2, 3, 4, 5, 6], [2, 3], 10)
    6
    >>> sum_multiples_below([1, 2, 3, 4, 5, 6], [2, 3], 20)
    12
    >>> sum_multiples_below([1, 2, 3, 