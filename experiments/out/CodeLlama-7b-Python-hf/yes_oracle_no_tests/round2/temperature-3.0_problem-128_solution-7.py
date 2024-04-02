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
    
	Do not include these tokens in the code: # return None if arr == []
	"""
    # pass
    # raise NotImplementedError()

    if len(arr) == 0:
        return None
    else:
        arr_signs = []
        for i in arr:
            if i == 0:
                arr_signs.append(0)
            elif i > 0:
                arr_signs.append(1)
            else:
                arr_signs.append(-1)
    
    return sum(arr) * (1 * arr_signs[0]) * (arr_signs[0] ** len(arr_signs))


print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))