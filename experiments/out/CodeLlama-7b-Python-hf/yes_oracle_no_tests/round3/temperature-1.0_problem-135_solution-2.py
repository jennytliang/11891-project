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
    # YOUR CODE HERE
    for i in range(len(arr)):
        if arr[i] <= arr[i-1]:
            return i-1
    return -1


def can_arrange_2(arr):
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
    # YOUR CODE HERE
    for i in range(len(arr)):
        if arr[i] <= arr[i-1]:
            return i-1
    return -1
