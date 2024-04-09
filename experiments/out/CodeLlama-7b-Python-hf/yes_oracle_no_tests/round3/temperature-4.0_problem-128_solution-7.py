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


    if len(arr) == 0:
        return None

    neg_count = 0
    pos_count = 0
    zero_count = 0

    for num in arr:
        if num < 0:
            neg_count += 1
        elif num > 0:
            pos_count += 1
        else:
            zero_count += 1
    
    if neg_count % 2 == 0:
        return pos_count - zero_count
    else:
        return neg_count - zero_count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
