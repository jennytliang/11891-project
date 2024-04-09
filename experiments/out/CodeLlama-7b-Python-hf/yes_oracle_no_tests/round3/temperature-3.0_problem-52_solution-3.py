def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    "*** YOUR CODE HERE ***"


def above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above or equal to threshold t.
    >>> above_threshold([1, 2, 4, 10], 100)
    False
    >>> above_threshold([1, 20, 4, 10], 5)
    True
    
	Include these tokens in the code: return all ( x >= t
	"""
    "*** YOUR CODE HERE ***"


def num_below_threshold(l: list, t: int):
    """Return the number of numbers in the list l that are below threshold t.
    >>> num_below_threshold([1, 2, 4, 10], 100)
    4
    >>> num_below_threshold([1, 20, 4, 10], 5)
    3
    
	Include these tokens in the code: return len(list(filter(lambda x: x < t, l))
	"""
    "*** YOUR CODE HERE ***"


def num_above_threshold(l: list, t: int):
    """Return the number of numbers in the list l that are above or equal to threshold t.
    >>> num_above_threshold([1, 2, 4, 10], 100)
    0
    >>> num_above_threshold([1, 20, 4, 10], 5)
    2
    
	Include these tokens in the code: return len(list(filter(lambda x: x >= t, l))
	"""
    "*** YOUR CODE HERE ***"


def max_of_list(l: list):
    """Return the maximum of the numbers in the list l.
    >>> max_of_list([1, 2, 4, 10])
    10
    >>> max_of_list([1, 20, 4, 10])
    20
    
	