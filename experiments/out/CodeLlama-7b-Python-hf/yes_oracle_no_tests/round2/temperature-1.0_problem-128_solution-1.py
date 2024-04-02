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
    if arr == []: return None
    sign_dict =  {-1:0, 0: 0, 1:0}
    for i in arr:
        if i > 0:
            sign_dict[1] += 1
            sign_dict[0] += 1
		# i < 0 but not -1
        if i < 0 and i != -1:
            sign_dict[1] += 1
            sign_dict[-1] += 1
        if i == -1:
            sign_dict[-1] += 1
	
    #return -1 * (sign_dict[-1]_mult_by_sign_dict[0]_, *sign_dict[-1]_mult_by_sign_dict[1]_ * sign_dict[0])
    
    #return -sum([sign_dict[-1] * sign_dict[1], sign_dict[-1] * sign_dict[0],[sign_dict[1] * sign_dict[0]]))
    #return (list(sign_dict.keys())[list(sign_dict.values()).index(max(sign_dict.values()))]* (-1 if list(sign_dict.keys()).index(min(sign_dict.keys())) != list(sign_dict.keys()).index(max(sign_dict.keys())) else 1))* reduce((lambda x, y: x * y), list(sign_dict.keys()))
    #return (list(sign_dict.keys())[list(sign_dict.keys()).index(min(sign_dict.keys()))] if sum(sign_dict.values()) != 3 else abs(list(sign_dict.keys())[list(sign_dict.keys()).index(min(sign_dict.keys()))]))* reduce((lambda x, y: x * y), list(sign_dict.keys()))   
    #return (list(sign_dict.keys())[list(sign_dict.values()).index(max(sign_dict.values()))] if sum(sign_dict.values()) != 3 else  abs(list(sign_dict.keys())[list(sign_dict.keys()).index(min(sign_