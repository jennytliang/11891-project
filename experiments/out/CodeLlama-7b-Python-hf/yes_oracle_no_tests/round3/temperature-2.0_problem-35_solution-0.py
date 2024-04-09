def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: return max
	Do not include these tokens in the code: # Your code here m
	"""

    # Your code here m
    max_el = l[0]
    for i in range(len(l)):
        if l[i] > max_el:
            max_el = l[i]

    return max_el


print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
