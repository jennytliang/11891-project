def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return maax_element(l, 0, len(l) - 1)

def max_element(l: list):
    if len(l) == 0:
        return None
    elif len(l) == 1:
        return l[0]
    else:
        mid = len(l) // 2
        left = l[0:mid]
        right = l[mid:]
        return max(max_element(left), max_element(right))
        
    




    





















































































































