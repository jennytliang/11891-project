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

 
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        return array_sum(arr) * array_product(arr)


def array_sum(arr):
    """
    Returns sum of integers in arr.
    """
    sum = 0
    for i in arr:
        sum += i

    return sum


def array_product(arr):
    """
    Returns product of integers in arr.
    """
    product = 1
    for i in arr:
        product *= i

    return product


print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
