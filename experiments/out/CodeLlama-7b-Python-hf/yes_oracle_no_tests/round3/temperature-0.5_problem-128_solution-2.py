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
    elif 0 in arr:
        re = 0
    else:
        re = sum([abs(num) for num in arr]) * (-1 if arr.count(-1) > arr.count(1) else 1)

    return re


if __name__ == "__main__":
    print(prod_signs([1, 2, 2, -4]))
    print(prod_signs([0, 1]))
    print(prod_signs([]))
