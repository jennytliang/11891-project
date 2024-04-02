def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Iter ate through the
	"""
    if len(arr) < 2:
        return -1
    idx = 0
    while idx < len(arr)-1:
        if arr[idx] >= arr[idx+1]:
            return -1
        idx += 1
    return idx
