def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    return all(x < t for x in l)

def same_sign(l: list):
    """Return True if all numbers in the list l have the same sign.
    >>> same_sign([1, 2, 4, 10])
    True
    >>> same_sign([1, -2, 4, 10])
    False
    
	Include these tokens in the code: return all ( x * y > 0
	"""
    return all(x * y > 0 for x in l for y in l)

def all_above(l1: list, l2: list):
    """Return True if every number in list l1 is above every number in list l2.
    >>> all_above([1, 3, 10, 15], [1, 2, 5, 10])
    True
    >>> all_above([1, 3, 10, 15], [1, 2, 6, 8])
    False
    
	Include these tokens in the code: return all ( x > y
	"""
    return all(x > y for x in l1 for y in l2)

def max_diff(l: list):
    """Return the maximum difference between two consecutive elements in l.
    >>> max_diff([10, 15, 20, 75, 80])
    35
    >>> max_diff([100, 50, 30])
    50
    
	Include these tokens in the code: max
	"""
    return max(x - y for x, y in zip(l[1:], l[:-1]))

def total(l: list):
    """Return the total of the numbers in l.
    >>> total([10, 15, 20, 75, 80])
    185
    >>> total([100, 50, 30])
    180
    
	Include these tokens in the code: sum
	"""
    return sum(l)

def mean(l: list):