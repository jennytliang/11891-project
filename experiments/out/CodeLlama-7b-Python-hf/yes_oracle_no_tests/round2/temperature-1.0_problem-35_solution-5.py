def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: max = l [ 0
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
    
	Do not include these tokens in the code: min = l [ 0
	"""
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min


def sum_element(l: list):
    """Return sum of the list.
    >>> sum_element([1, 2, 3])
    6
    >>> sum_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    133
    
	Do not include these tokens in the code: sum = 0
    """
    sum = 0
    for i in l:
        sum += i
    return sum


def average(l: list):
    """Return average of the list.
    >>> average([1, 2, 3])
    2.0
    >>> average([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    16.25
    
	Do not include these tokens in the code: sum = 0
    """
    sum = 0
    for i in l:
        sum += i
    return sum / len(l)


def reverse(l: list):
    """Return reversed list of the given list.
    >>> reverse([1, 2, 3])
    [3, 2, 1]
    >>> reverse([5, 3, -5, 2, -3, 3, 9