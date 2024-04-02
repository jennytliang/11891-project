def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len
	Do not include these tokens in the code: if
	"""
    # Your code here
    # pass
    # max_arr = max(arr)
    # for i in range(len(arr)):
    #     if arr[i] <= max_arr:
    #         return i
    # return -1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] <= arr[i]:
                return j
    return -1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
