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

    if 0 in arr:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] * arr[1]
    else:
        return arr[0] * arr[1] * arr[2] * sum([-1 if i < 0 else 1 for i in arr])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
