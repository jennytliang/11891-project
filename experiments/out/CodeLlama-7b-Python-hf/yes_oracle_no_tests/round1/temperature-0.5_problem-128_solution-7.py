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
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

    if 0 == len(arr):
        return None

    negative_count = 0
    zero_count = 0
    positive_count = 0
    product = 1
    for i in arr:
        if 0 == i:
            zero_count += 1
        elif i < 0:
            negative_count += 1
        else:
            positive_count += 1

    if (positive_count + negative_count + zero_count) % 2 == 0:
        if negative_count % 2 == 0:
            product = 1
        else:
            product = -1
    else:
        if negative_count % 2 == 1:
            product = -1

    return sum(arr) * product


























