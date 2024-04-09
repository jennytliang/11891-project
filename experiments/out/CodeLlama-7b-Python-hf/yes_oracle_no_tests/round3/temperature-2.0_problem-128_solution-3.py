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
    # check if the array is empty
    if arr == []:
        return None
    # initialize the variables
    sum_signs = 0
    prod_signs = 1
    # loop through the array
    for x in arr:
        # check if the number is 0
        if x == 0:
            sum_signs += 0
            prod_signs = 0
        # check if the number is positive
        if x > 0:
            sum_signs += x
            prod_signs *= 1
        # check if the number is negative
        if x < 0:
            sum_signs += -x
            prod_signs *= -1
    # return the sum of the magnitudes of integers multiplied by product of all signs of each number in the array
    return sum_signs * prod_signs


print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
