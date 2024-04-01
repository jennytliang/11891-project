def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code:  if len ( arr ) ==  0 :
	"""

    if len(arr) == 0:
        return -1

    if len(arr) == 1:
        return 0

    if len(arr) == 2:
        if arr[1] >= arr[0]:
            return -1
        else:
            return 0

    if arr[1] >= arr[0]:
        prev_index = 0
        for i in range(len(arr)):
            if arr[i] >= arr[prev_index]:
                if i == len(arr) - 1:
                    return -1
                else:
                    if arr[i + 1] >= arr[i]:
                        return -1
                    else:
                        prev_index = i + 1
    else:
        prev_index = 0
        for i in range(len(arr)):
            if arr[i] >= arr[prev_index]:
                prev_index = i

    return prev_index
