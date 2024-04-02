def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: return max ( l )
	"""
    return max(l)


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Include these tokens in the code: return min ( l )
	"""
    return min(l)


def reverse_list(l: list):
    """Return reversed list.
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    >>> reverse_list(['alice', 'bob', 'chris'])
    ['chris', 'bob', 'alice']
    
	Include these tokens in the code: l.reverse ()
	"""
    l.reverse()
    return l


def list_length(l: list):
    """Return length of the list.
    >>> list_length([1, 2, 3])
    3
    >>> list_length(['alice', 'bob', 'chris'])
    3
    
	Include these tokens in the code: return len ( l )
	"""
    return len(l)


def list_contains(l: list, element):
    """Return whether list contains element.
    >>> list_contains([1, 2, 3], 1)
    True
    >>> list_contains(['alice', 'bob', 'chris'], 'bob')
    True
    >>> list_contains([1, 2, 3], 7)
    False
    >>> list_contains(['alice', 'bob', 'chris'], 'john')
    False
    
	Include these tokens in the code: return element in l
	"""
    return element in l


def list_sum(l: list):
    """Return sum of the elements in the list.
    >>> list_sum([1, 2, 3])
    6
    >>> list