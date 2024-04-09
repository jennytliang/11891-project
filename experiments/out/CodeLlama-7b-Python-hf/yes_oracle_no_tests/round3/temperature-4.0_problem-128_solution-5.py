def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    
	Do not include these tokens in the code: # pass #
	"""
    if len(arr) == 0:
        return None
    result = 0
    for i in arr:
        if i < 0:
            result += i
        elif i > 0:
            result += 1
    return result * arr[0] * arr[1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
