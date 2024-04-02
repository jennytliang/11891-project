def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: max _ element = l [ 0
	"""
    max_elem = l[0]
    for elem in l:
        if elem > max_elem:
            max_elem = elem
    return max_elem

print(F"max_element.py: max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) = 123 = {max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])}")