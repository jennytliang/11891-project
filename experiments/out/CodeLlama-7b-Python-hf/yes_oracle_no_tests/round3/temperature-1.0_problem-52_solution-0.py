def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    return all(x < t for x in l)


def same_sign(x: int, y: int):
    """Check if x and y have the same sign.
    >>> same_sign(1, 1)
    True
    >>> same_sign(-1, 1)
    False
    >>> same_sign(1, 100)
    True
    >>> same_sign(-1, -100)
    True
    >>> same_sign(1, -1)
    False
    >>> same_sign(-1, -1)
    True
    """
    return x * y > 0


def count_positives(nums: list):
    """Return the count of positive numbers in nums.
    >>> count_positives([1, 2, 3, -4, 5, -6, -7, 8, -9, -10])
    5
    >>> count_positives([1, -1, -2, -3, -4, -5, -6, -7])
    1
    >>> count_positives([-1, -2, -3, -4, -5, -6, -7, -8])
    0
    >>> count_positives([0, 0, 0, 0, 0, 0, 0, 0])
    1
    >>> count_positives([0, 0, 0, 1, 1, 1, 1, 1])
    2
    
	Include these tokens in the code: return all (x >= 0
	"""
    return len([x for x in nums if x >= 0])


def all_same_sign(nums: list):
    """Check if all numbers in nums have the same sign.
    >>> all_same_sign([1, 2, 3, -4, 5, -6, -7, 8, -9, -10])
    False
    >>> all_same_sign([1, -1, -2, -3, -4, -5, -6, -7