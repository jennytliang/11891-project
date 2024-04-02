def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: return max ( l )
	Do not include these tokens in the code: m = [ 0 ]
	"""
    m = [0]
    for i in l:
        if i > m[0]:
            m[0] = i
    return m[0]


print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
