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
    if arr == []:
        return None
    else:
        signs = [1 if i > 0 else 0 if i == 0 else -1 for i in arr]
        signed_nums = [i if i > 0 else 0 if i == 0 else -i for i in arr]
        product = 1
        for i in signed_nums:
            product *= i
        return sum(signs) * product


if __name__ == "__main__":
    import doctest

    doctest.testmod()
