def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    return all(x < t for x in l)


def only_evens(l: list):
    """Return a list that includes only the even elements of l.
    >>> only_evens([1, 2, 4, 5, 10])
    [2, 4, 10]
    
	Include these tokens in the code: return all ( x is even
	"""
    return [x for x in l if x % 2 == 0]


def only_odds(l: list):
    """Return a list that includes only the odd elements of l.
    >>> only_odds([1, 2, 4, 5, 10])
    [1, 5]
    
	Include these tokens in the code: return all ( x is odd
	"""
    return [x for x in l if x % 2 != 0]


def multiples_of_three(l: list):
    """Return a list that includes only the multiples of three in l.
    >>> multiples_of_three([3, 5, 6, 9, 10, 12])
    [3, 9, 12]
    
	Include these tokens in the code: return all ( x % 3 == 0
	"""
    return [x for x in l if x % 3 == 0]


def multiples_of_five(l: list):
    """Return a list that includes only the multiples of five in l.
    >>> multiples_of_five([3, 5, 6, 9, 10, 12])
    [5, 10, 12]
    
	Include these tokens in the code: return all ( x % 5 == 0
	"""
    return [x for x in l if x % 5 == 0]


def multiples_of_three_or_five(l: list):
    """Return a list that includes only the multiples of three or five in l.
    >>> multiples_of_three_or_five([3, 