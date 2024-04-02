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
    
	Include these tokens in the code: if 0 in arr
	Do not include these tokens in the code: else
	"""

    if arr == []:
        re = None
    else:
        re = 0
        for item in arr:
            if item == 0:
                re = re + 1
            if item > 0:
                re = re + 1
            if item < 0:
                re = re - 1

        if re == 0:
            re = 1
        if re > 0:
            re = re * -1
    return re


print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
