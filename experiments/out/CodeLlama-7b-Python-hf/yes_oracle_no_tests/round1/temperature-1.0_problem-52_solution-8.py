def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    result = True
    for x in l:
        if x < t:
            continue
        else:
            result = False
    return result



def count_below_threshold(l: list, t: int):
    """Return the number of values that are less than threshold t.
    >>> count_below_threshold([1, 2, 4, 10], 100)
    3
    >>> count_below_threshold([1, 2, 3, 4], 5)
    4
    >>> count_below_threshold([], 1)
    0
    """
    result = 0
    for x in l:
        if x < t:
            result = result + 1
    return result



def above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> above_threshold([1, 2, 4, 10], 1)
    False
    >>> above_threshold([1, 20, 4, 10], 5)
    True
    
	Include these tokens in the code: return all (x > t
	"""
    result = True
    for x in l:
        if x < t:
            result = False
        else:
            continue
    return result



def count_above_threshold(l: list, t: int):
    """Return the number of values that are above or equal to threshold t.
    >>> count_above_threshold([1, 2, 4, 10], 1)
    3
    >>> count_above_threshold([1, 20, 4, 10], 5)
    2
    >>> count_above_threshold([], 1)
    0
    """

    result = 0
    for x in l:
        if x >= t:
            result = result + 1
    return result



# Examples of function calls
print(str(below_threshold([1, 2, 4], 10