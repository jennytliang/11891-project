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
    # pass
    # take a look at the tests tab for more examples
    if arr == []:
        return None
    else:
        prod = 1
        for i in arr:
            if i > 0:
                prod *= 1
            elif i < 0:
                prod *= -1
            else:
                prod *= 0
        res = 1
        for i in arr:
            if i > 0:
                res *= 1
            elif i < 0:
                res *= -1
            else:
                res *= 0
        return res * prod


if __name__ == '__main__':
    print('Example:')
    print(prod_signs([1, 2, 2, -4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) == None
    print('Wow, you are doing pretty good. Time to check it!')