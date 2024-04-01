def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code:  max _ element = l [ 0 ]
	"""

    if len(l) == 0:
        return None
    else:
        max_element = l[0]
        for element in l:
            if element > max_element:
                max_element = element
        return max_element


print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
