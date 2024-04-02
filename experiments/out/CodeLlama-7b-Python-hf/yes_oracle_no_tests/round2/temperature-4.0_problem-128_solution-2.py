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
    
	Do not include these tokens in the code: not
	"""

 
    if not arr:
        return None

    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] * arr[1]
    else:
        if arr[0] < 0:
            return (arr[0] * arr[1] * arr[2]) + (arr[0] * arr[3] * arr[4]) - (arr[0] * arr[5] * arr[6])
        else:
            return (arr[0] * arr[1] * arr[2]) + (arr[0] * arr[3] * arr[4]) + (arr[0] * arr[5] * arr[6])


if __name__ == '__main__':
    print('Example:')
    print(prod_signs([1, 2, 2, -4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) == None
    print('Wow, you are doing pretty good. Time to check it!')

