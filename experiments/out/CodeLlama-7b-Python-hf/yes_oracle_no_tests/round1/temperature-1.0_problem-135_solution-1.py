def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: if len ( arr ) ==
	"""
    _max = max(arr)
    temp = [-1] * (_max + 1)
    for i, elem in enumerate(arr):
        if temp[elem - 1] == -1:
            temp[elem-1] = 0
        else:
            temp[elem-1] += 1
        if temp[elem] == 0:
            temp[elem] = i+1
        else:
            temp[elem-1] += arr[temp[elem-1]] - temp[elem]
    for i in range(len(temp)):
        temp[i] = temp[i] if temp[i] < 0 else -1
    return temp
    # _max = max(arr)
    # _min = min(arr, default = 0)
    # temp = [-1] * (_max+1)
    # for i, elem in enumerate(arr):
    #     if temp[elem-1] == -1:
    #         temp[elem-1] = i
    #     else:
    #         if temp[elem] == -1:
    #             temp[elem] = i
    #         else:
    #             if elem <= arr[temp[elem]]:
    #                 temp[elem] = i
    #         if temp[elem-1] < temp[elem]:
    #             temp[elem-1] = temp[elem]
    # return -1