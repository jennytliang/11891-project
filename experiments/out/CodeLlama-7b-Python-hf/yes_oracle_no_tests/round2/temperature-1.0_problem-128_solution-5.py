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
    
	Include these tokens in the code: if arr == [] : return None if
	"""

    if arr == []: return None

    signs = [1 if x >= 0 else -1 for x in arr]
    signs = 1 if all(signs) else -1
    
    return signs * (1 if signs == 1 else -1) * sum(num ** 2 for num in arr)

def prod_signs1(arr):
    return (-1 if sum(map(lambda x: -1 if x > 0 else 1 if x < 0 else 0, arr)) == -len(filter(lambda x: x < 0, arr)) else 1) * sum(map(lambda x: x ** 2, arr)) if len(arr) != 0 else None

    