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
    
	Include these tokens in the code: if arr == [] : return None
	"""
    if arr == []:
        return None
    else:
        return sum(arr) * (1 if arr[0] > 0 else -1 if arr[0] < 0 else 0) * reduce(lambda x, y: x * y, [1 if i > 0 else -1 if i < 0 else 0 for i in arr])
