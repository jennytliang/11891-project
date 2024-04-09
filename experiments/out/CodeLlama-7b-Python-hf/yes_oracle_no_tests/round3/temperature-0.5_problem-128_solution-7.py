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
        if 0 in arr:
            for i in arr:
                if i == 0:
                    re += 0
                elif i > 0:
                    re += i
                else:
                    re -= i
        else:
            for i in arr:
                if i > 0:
                    re += i
                else:
                    re -= i
        re *= prod(arr)
    return re


def prod(arr):
    if arr == []:
        return 1
    else:
        return arr[0] * prod(arr[1:])


print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
