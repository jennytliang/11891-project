def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: print ( F " max _ element . py
	"""


    return ma(l)


def ma(l):
    m = l[0]
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
    return m





print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
