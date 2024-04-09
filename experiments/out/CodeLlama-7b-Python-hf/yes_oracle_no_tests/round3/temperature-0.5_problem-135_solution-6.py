def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len
	Do not include these tokens in the code: # TODO : Write your code here
	"""

    # TODO : Write your code here
    n = len(arr)
    if n < 2:
        return -1
    max_val = arr[0]
    max_idx = 0
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
        elif arr[i] == max_val:
            if i < max_idx:
                max_idx = i
    return max_idx


def can_arrange_2(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len
	Do not include these tokens in the code: # TODO : Write your code here
	"""

    # TODO : Write your code here
    n = len(arr)
    if n < 2:
        return -1
    max_val = arr[0]
    max_idx = 0
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
        elif arr[i] == max_val:
            if i < max_idx:
                max_idx = i
    return max_idx


def can_arrange_3(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1