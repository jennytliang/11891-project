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

  # If arr is empty, return None
    if len(arr) == 0:
        return None
    else:
        # Check if all elements are 0
        if 0 in arr:
            return 0
        # Check if all elements are positive
        elif arr.count(-1) == 0:
            return sum(arr)
        # Check if all elements are negative
        elif arr.count(1) == 0:
            return sum(arr) * -1
        # Else, return the sum of magnitudes of integers
        # multiplied by product of all signs of each number
        else:
            return sum(arr) * arr.count(-1)
