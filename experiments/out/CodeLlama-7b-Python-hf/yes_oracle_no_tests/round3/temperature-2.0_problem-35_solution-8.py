def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	"""



    
    ret = l[0]
    for i in l:
        if i > ret:
            ret = i
    return ret

    
    
    
def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	"""

    
    
    
    
def sum_element(l: list):
    """Return sum of all the elements in the list.
    >>> sum_element([1, 2, 3])
    6
    >>> sum_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    125
    
	"""
    
    
    
    
    
def reverse_list(l: list):
    """Return the list in reverse order.
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    >>> reverse_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-10, 1, 9, 3, 3, -3, 2, -5, 3, 5]
    
	"""
    
    
    
    
    
def sort_list(l: list):
    """Return a sorted list.
    >>> sort_list([1, 2, 3])
    [1, 2, 3]
    >>> sort_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-10, -3, -3, -5, 0, 1, 2, 3, 3, 9, 123]