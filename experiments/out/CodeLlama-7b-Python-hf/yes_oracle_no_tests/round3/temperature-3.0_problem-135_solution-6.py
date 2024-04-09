def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Find the largest index of an
	"""
    def find_largest_index(arr):
        for i in range(len(arr)-1, -1, -1):
            if arr[i] <= arr[i-1]:
                return i
        return -1
    
    l = find_largest_index(arr)
    if l == -1:
        return -1
    else:
        r = find_largest_index(arr[:l:-1])
        return len(arr)-1-r if r != -1 else -1







































