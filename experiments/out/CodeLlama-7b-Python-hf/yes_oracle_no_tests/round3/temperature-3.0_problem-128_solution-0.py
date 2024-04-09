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
	"""


    
    if arr == []:
 
        return None

    if 0 in arr:
        return 0

    else:
        prod = 1
        sum = 0
        for i in arr:
            if i > 0:
                sum += i
                prod *= 1
            elif i < 0:
                sum += i
                prod *= -1
            else:
                sum = 0
                prod *= 0
        return sum * prod




print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))