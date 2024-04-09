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
    return False

def sum_multiples(l: list, n: int):
    """Return the sum of all the elements in l that are multiples of n.
    >>> sum_multiples([2, 4, 5, 10, 11, 12, 15], 3)
    30
    >>> sum_multiples([2, 4, 5, 10, 11, 12, 15], 5)
    20
    >>> sum_multiples([2, 4, 5, 10, 11, 12, 15], 7)
    0
    """
    return sum([x for x in l if x % n == 0])

def sum_below_threshold(l: list, t: int):
    """Return the sum of all the elements in l that are below threshold t.
    >>> sum_below_threshold([1, 2, 4, 10], 100)
    13
    >>> sum_below_threshold([1, 20, 4, 10], 5)
    5
    """
    return sum([x for x in l if x < t])

def max_in_list(l: list):
    """Return the maximum value in the list l.
    >>> max_in_list([1, 2, 4, 10, 11, 12, 15])
    15
    >>> max_in_list([1, 2, 4, 10, 11, 12, 15, -5])
    15
    >>> max_in_list([-1, -2, -4, -10, -11, -12, -15])
    -1
    """
    return max(l)

def max_of_three(a: int, b: int, c: int):
    """Return the maximum of the three arguments.
    >>> max_of_three(1,