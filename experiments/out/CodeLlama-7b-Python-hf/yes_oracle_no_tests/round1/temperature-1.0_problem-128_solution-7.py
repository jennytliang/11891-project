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

 

def prod_signs(arr):
    signs = []
    for i in arr:
        if i > 0:
            signs.append(1)
        elif i < 0:
            signs.append(-1)
        elif i == 0:
            signs.append(0)
    prod = 1
    for i in signs:
        if i == 1 or i == -1:
            prod = 1*prod*i
        elif i == 0:
            return 0
    return prod

#assert prod_signs([1, 2, 2, -4]) == -9
#assert prod_signs([0, 1]) == 0
#assert prod_signs([]) == None