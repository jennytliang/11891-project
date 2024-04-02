def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: return max
	Do not include these tokens in the code: m = l [ 0 ]
	"""
    max = l[0]
    for x in l:
        if x > max:
            max = x
    return max
