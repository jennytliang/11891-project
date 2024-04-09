def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    for x in l:
        if x >= t:
            return False

    return True


def has_seven(n: int):
    """Returns True if n has a digit that equals 7
    >>> has_seven(7)
    True
    >>> has_seven(37)
    True
    >>> has_seven(31321)
    False
    >>> has_seven(3737373)
    True
    """

    n_str = str(n)

    for s in n_str:
        if int(s) == 7:
            return True

    return False


def make_pi():
    """Returns a list of the first 10,000 decimal digits of pi.
    >>> make_pi()
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 6, 5, 9, 2, 1, 3, 1, 2, 9, 2, 9, 9, 5, 9, 9, 9]
    """

    import math

    pi = math.pi
    pi_str = str(pi)
    pi_list = list(pi_str)

    return pi_list


def cumulative_sum(l: list):
    """Return a new list containing the cumulative sum of the items in l.
    >>> cumulative_sum([1, 1, 1, 1, 1])
    [1, 2, 3, 4, 5]
    >>> cumulative_sum([100, 1, 1, 1