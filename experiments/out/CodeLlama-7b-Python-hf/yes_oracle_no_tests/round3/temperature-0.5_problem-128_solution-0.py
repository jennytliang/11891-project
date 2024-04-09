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
    
	Include these tokens in the code: if 0 in arr : return 0
	Do not include these tokens in the code: else
	"""

    if arr == []:
        re = None
        return re

    else:
        arr_signs = []
        for i in range(len(arr)):
            if arr[i] > 0:
                arr_signs.append(1)
            elif arr[i] < 0:
                arr_signs.append(-1)
            elif arr[i] == 0:
                arr_signs.append(0)

        arr_signs_prod = 1
        for i in range(len(arr_signs)):
            arr_signs_prod = arr_signs_prod * arr_signs[i]

        arr_nums_sum = 0
        for i in range(len(arr)):
            arr_nums_sum = arr_nums_sum + abs(arr[i])

        re = arr_nums_sum * arr_signs_prod
        return re


print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
