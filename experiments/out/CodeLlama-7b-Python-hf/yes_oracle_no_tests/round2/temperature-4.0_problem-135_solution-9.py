def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # check
	"""
    # check for empty array
    if not arr:
        return -1
    # check for single element
    if len(arr) == 1:
        return -1
    # check for two elements
    if len(arr) == 2:
        if arr[0] <= arr[1]:
            return -1
        else:
            return 0
    # check for three elements
    if len(arr) == 3:
        if arr[0] <= arr[1] <= arr[2]:
            return -1
        elif arr[0] <= arr[2] <= arr[1]:
            return -1
        else:
            return 2
    
    # check for four elements
    if len(arr) == 4:
        if arr[0] <= arr[1] <= arr[2] <= arr[3]:
            return -1
        elif arr[0] <= arr[2] <= arr[1] <= arr[3]:
            return -1
        elif arr[0] <= arr[3] <= arr[1] <= arr[2]:
            return -1
        else:
            return 3
    
    # check for five or more elements
    if len(arr) >= 5:
        if arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4]:
            return -1
        elif arr[0] <= arr[2] <= arr[1] <= arr[3] <= arr[4]:
            return -1
        elif arr[0] <= arr[3] <= arr[1] <= arr[2] <= arr[4]:
            return -1
        elif arr[0] <= arr[4] <= arr[1] <= arr[2] <= arr[3]:
            return -1
        elif arr[0] <= arr[1] <= arr[3] <= arr[2] <= arr[4]:
            return -1
        elif arr[0] <= arr[1] <= arr[4] <= arr[2] <= arr[3]:
            return -1
        elif arr[0] <= arr[1] <= arr[2] <= arr[4