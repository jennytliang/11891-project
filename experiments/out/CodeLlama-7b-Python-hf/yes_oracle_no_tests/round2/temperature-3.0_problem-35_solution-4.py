def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: return max ( l )
	"""
    return max(l)


def reverse(l: list):
    """Return reversed list.
    >>> reverse([1, 2, 3])
    [3, 2, 1]
    >>> reverse([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-10, 1, 9, 3, 3, -3, 2, -5, 3, 5]
    
	Include these tokens in the code: l.reverse ()
	"""
    l.reverse()
    return l


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Include these tokens in the code: return min ( l )
	"""
    return min(l)


def reverse_and_max(l: list):
    """Return maximum element in the reversed list.
    >>> reverse_and_max([1, 2, 3])
    3
    >>> reverse_and_max([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: return max ( l )
	"""
    l.reverse()
    return max(l)


def reverse_and_min(l: list):
    """Return minimum element in the reversed list.
    >>> reverse_and_min([1, 2, 3])
    3
    >>> reverse_and_min([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Include these tokens in the code: return min