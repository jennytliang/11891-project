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
    sum_sign = 0
    is_neg_flag = 0
    is_zero_flag = 0
    
    for i in arr:
        if (i is not 0):
            if (i < 0):
                is_neg_flag = 1
            else:
                is_neg_flag = 0
        if (i is 0):
            is_zero_flag = 1
        else:
            is_zero_flag = 0
            num = abs(i)
            sum_sign += num
    if (is_neg_flag):
        if (is_zero_flag):
            sign_prod = 0
        else:
            sign_prod = -1 * sum_sign
    else:
        sign_prod = sum_sign
    return(sign_prod)
    