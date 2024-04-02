def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: max _ element = l [ 0
	"""
    
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Do not include these tokens in the code: min _ element = l [ 0
	"""
    
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

def reverse(l: list):
    """Return the list in reversed order.
    >>> reverse([1, 2, 3])
    [3, 2, 1]
    >>> reverse([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-10, 1, 9, 3, 3, -3, 2, -5, 5, 3, 123, 0]
    
	Do not include these tokens in the code: reverse l [ : :: -1
	"""
    
    return l[::-1]

def is_sorted(l: list):
    """Return whether the list is sorted.
    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([1, 2, 1])
    False
    
	Do not include these tokens in the code: sorted
	"""
    
    return l == sorted(l)

def bubble_sort(l: list):
    """Return the list sorted in ascending order.
    >>> bubble_sort([1, 2, 3])
    [1, 2, 3]
    >>> bubble_sort([1, 2, 1])
    [1, 1, 2]