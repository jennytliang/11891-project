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
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] * arr[1]
    
    counter = 0
    counter_neg = 0
    counter_zero = 0
    for i in arr:
        if i > 0:
            counter += 1
        elif i == 0:
            counter_zero += 1
        else:
            counter_neg += 1
    
    if counter == len(arr):
        return 1
    if counter_neg == len(arr):
        return -1
    if counter_zero == len(arr):
        return 0
    
    if (counter_neg == 0 and counter == len(arr)) or (counter_neg == 0 and counter_zero == len(arr)):
        return 1
    if (counter_neg == 0 and counter_zero == len(arr)) or (counter == 0 and counter_zero == len(arr)):
        return -1
    if counter_neg == 0 and counter_zero == 0:
        return 1
    if counter_neg == 0 and counter == 0:
        return -1
    if counter_neg == 0 and counter_zero == 0:
        return 1
    if counter_neg == 0 and counter == 0:
        return -1
    if counter_neg == 0 and counter_zero == 0:
        return 1
    
    
    # if counter_neg == 0 and counter == 0:
    #     return -1
    # if counter_neg == 0 and counter_zero == 0:
    #     return 1
    
    # if (counter_neg == 0 and counter == len(arr)) or (counter_neg == 0 and counter_zero == len(arr)):
    #     return 1
    # if (counter_neg == 0 and counter == len(arr)) or (counter == 0 and counter_zero == len(arr)):
    #     return -1
