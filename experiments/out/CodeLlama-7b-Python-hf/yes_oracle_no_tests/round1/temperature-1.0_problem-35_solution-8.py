def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return max(l)


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return min(l)


def sum_element(l: list):
    """Return sum of all elements in the list.
    >>> sum_element([1, 2, 3])
    6
    >>> sum_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    130
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return sum(l)


def average(l: list):
    """Return average of all elements in the list.
    >>> average([1, 2, 3])
    2.0
    >>> average([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    22.6
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return sum(l) / len(l)


def length(l: list):
    """Return number of elements in the list.
    >>> length([1, 2, 3])
    3
    >>> length([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    11
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return len(l)


def reverse(l: list):
    """