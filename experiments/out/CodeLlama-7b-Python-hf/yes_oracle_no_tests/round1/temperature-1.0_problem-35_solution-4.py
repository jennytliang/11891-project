def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return max(l)

    # Alternative solutions
    if len(l) == 1:
        return l[0]
    elif len(l) == 0:
        raise ValueError
    else:
        largest = None
        for i in l:
            if largest is None or i > largest:
                largest = i

        return largest

    # Alternative solutions using reduce
    def compare(a, b):
        if a > b:
            return a
        else:
            return b

    return reduce(compare, l)
