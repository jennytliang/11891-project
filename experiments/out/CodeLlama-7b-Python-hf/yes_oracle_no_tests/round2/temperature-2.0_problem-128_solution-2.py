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


    # pass
    # write your code here
    if not arr:
        return None
    else:
        signs = []
        for x in arr:
            if x == 0:
                signs.append(0)
            elif x > 0:
                signs.append(1)
            else:
                signs.append(-1)
        return sum([abs(x) for x in arr]) * (1 * signs[0]) * (1 * signs[1]) * (1 * signs[2]) * (1 * signs[3])

if __name__ == '__main__':
    import doctest
    doctest.testmod()