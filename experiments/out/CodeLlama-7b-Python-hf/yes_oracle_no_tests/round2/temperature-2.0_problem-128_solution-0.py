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
    
	Include these tokens in the code: if arr == [] : return None if
	"""
    if arr == []: return None
    if len(arr) == 1: return arr[0]
    if len(arr) == 2: return arr[0] * arr[1]
    if len(arr) == 3: return arr[0] * arr[1] * arr[2]
    if len(arr) == 4: return arr[0] * arr[1] * arr[2] * arr[3]
    
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]
    if a == 0:
        if b == 0:
            if c == 0:
                return d
            else:
                return c
        else:
            if d == 0:
                return b
            else:
                return b * d
    else:
        if b == 0:
            if c == 0:
                return a
            else:
                return a * c
        else:
            if d == 0:
                return a * b
            else:
                return a * b * d


if __name__ == '__main__':
    print('Example:')
    print(prod_signs([1, 2, 2, -4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) == None
    print('You are awesome! All tests are done! Go Check it!')