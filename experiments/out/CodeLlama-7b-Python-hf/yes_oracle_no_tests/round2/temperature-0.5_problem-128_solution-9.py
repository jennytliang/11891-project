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
    # return None if arr == []

    # if len(arr) < 1:
    #     return None

    # if len(arr) == 1:
    #     return arr[0]

    # if len(arr) == 2:
    #     return arr[0] * arr[1]

    # if len(arr) == 3:
    #     return arr[0] * arr[1] * arr[2]

    # if len(arr) == 4:
    #     return arr[0] * arr[1] * arr[2] * arr[3]

    # if len(arr) == 5:
    #     return arr[0] * arr[1] * arr[2] * arr[3] * arr[4]

    # if len(arr) == 6:
    #     return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5]

    # if len(arr) == 7:
    #     return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6]

    # if len(arr) == 8:
    #     return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7]

    # if len(arr) == 9:
    #     return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8]

    # if len(arr) == 10:
    #     return arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9]

    # if len(arr) == 11:
    #     return arr[0] * arr[1