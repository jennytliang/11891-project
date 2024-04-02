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

    # If array is empty return None
    if arr == []:
        return None

    # Define empty array to store signs
    signs = []

    # Loop through array
    for i in arr:

        # Check if number is zero. If so, append 0 to signs array
        if i == 0:
            signs.append(0)

        # Check if number is negative. If so, append -1 to signs array
        elif i < 0:
            signs.append(-1)

        # Check if number is positive. If so, append 1 to signs array
        elif i > 0:
            signs.append(1)

    # Multiply signs array
    mult = 1
    for i in signs:
        mult = mult * i

    # Multiply numbers in array by product of signs
    final = 0
    for i in arr:
        final = final + i * mult

    # Return result
    return final


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
    """
    if not arr:
        return None
    signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
    return sum(i * j for i, j in zip(arr, reduce(lambda x, y: x * y, signs, 1)))
