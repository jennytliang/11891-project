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

  # if arr is empty
    if not arr:
        return None

  # get the product of the signs of the array
    product = 1
    for num in arr:
        if num > 0:
            product *= 1
        elif num < 0:
            product *= -1
        else:
            product *= 0

  # get the sum of the magnitudes of the array
    sum = 0
    for num in arr:
        sum += abs(num)

  # return the product of the signs multiplied by the sum of the magnitudes
    return product * sum


# print(prod_signs([1, 2, 2, -4]))
# print(prod_signs([0, 1]))
# print(prod_signs([]))
