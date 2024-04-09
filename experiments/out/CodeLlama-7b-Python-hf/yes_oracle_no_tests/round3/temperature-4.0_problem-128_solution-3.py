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
    
	Do not include these tokens in the code: ret ur None return
	"""


    if arr  == []:
        return None
    else:
        if arr[0] == 0:
            return 0
        elif arr[0] < 0:
            return sum([-1 * i for i in arr]) * (-1)
        else:
            return sum(arr) * (-1)


print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))


