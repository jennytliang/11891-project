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
    # return None if arr == []
    if arr == []:
        return None

    # Set variables to be used later
    signs = []
    mag_sum = 0

    # For loop to loop through each element in arr
    for i in arr:
        if i > 0:
            signs.append(1)
        elif i == 0:
            signs.append(0)
        else:
            signs.append(-1)

    # For loop to loop through each element in signs
    for i in signs:
        if i == 0:
            continue

        # Multiply the element in signs by the absolute value of the
        # element in arr
        mag_sum += i * abs(arr[signs.index(i)])

    # Multiply the sum of magnitudes by the product of the signs
    return mag_sum * (signs.count(1) / signs.count(-1))


# Pybites solution


def prod_signs1(arr):
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
    # return None if arr == []
    if not arr:
        return None

    # Set variables to be used later
    signs = []
    mag_sum = 0

    # For loop to loop through each element in arr
    for i in arr:
        if i > 0:
            signs.append(1)
        elif i == 0:
            signs.append(0)
        else:
            signs.append(-1)

    # For loop to loop through each element in signs
    for