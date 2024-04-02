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
	Do not include these tokens in the code: def prod _ sign
	"""
    sums = 0
    if arr == []:
        return None
    for i in arr:
        if i < 0:
            sums += i * -1
        elif i > 0:
            sums += i
        else:
            sums += i
    
    prods = sums * 1
    return prods
  
prod_signs([1, 2 , -2, 4])