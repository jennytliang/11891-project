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
    def can_arrange_helper(arr, i, prev):
        if i >= len(arr):
            return prev < arr[i-1]
        return can_arrange_helper(arr, i+1, max(prev, arr[i]))
    return can_arrange_helper(arr, 1, arr[0])
