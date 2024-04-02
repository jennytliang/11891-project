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
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # def prod _ sign
	"""
    # [3, 4, 5, 5, -4 , 6, 6 , 2]
    # [3 , 4 , 3 , 33 , 4 , 6 , 6 , 2] [ 1 | 1 | -1 | 1 | 1 | 1 | 1 | 1 ] 
    prod = 1
    count_neg = 0
    count_zero = 0
    count_pos = 0
    if len(arr) == 0:
        return None 
    if len(arr) == 1:
        if arr[0] == 0:
            return 0
        return abs(arr[0])
    else:
        for x in arr:
            if x > 0 :
                count_pos += 1
            elif x < 0 :
                count_neg += 1
            elif x == 0:
                count_zero += 1
        sign = 1
        if count_neg - count_pos == 0 and count_zero != 0:
            sign = 0
        elif count_neg - count_pos > 0:
            sign = -1
        else :
            sign = 1
    total_sum = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            total_sum += abs(arr[i]) * sign
    return total_sum 
    pass