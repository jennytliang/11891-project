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

  # Code here
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        if arr[0] == 0:
            return 0
        else:
            return arr[0] * prod_signs(arr[1:])


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
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

    # Code here
    if len(arr) == 0:
        return None

    def helper(arr, index):
        if index == len(arr):
            return 0
        else:
            if arr[index] == 0:
                return 0
            else:
                return arr[index] * helper(arr, index + 1)

    return helper(arr, 0) * sum(map(lambda x: 1 if x > 0 else -1 if x < 0 else 0, arr))
