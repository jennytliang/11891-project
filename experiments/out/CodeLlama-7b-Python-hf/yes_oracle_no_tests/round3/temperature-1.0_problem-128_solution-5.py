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
    
	Include these tokens in the code: if 0 in arr : return
	Do not include these tokens in the code: result =
	"""

    if arr == []:
        re = None
    else:
        re = 0
        for i in arr:
            if i == 0:
                re += 0
            if i > 0:
                re += 1
            if i < 0:
                re -= 1
        re = re * (abs(arr[0]) * abs(arr[1]))
        for i in arr[1:]:
            re *= abs(i)
    return re


if __name__ == "__main__":
    import doctest

    doctest.testmod()
