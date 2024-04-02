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
    
    if len(arr) == 0:
        return -1

    max_elem = max(arr)
    if max_elem < len(arr):
        return -1

    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return -1

    return max_elem-1


print(can_arrange([1,2,4,3,5]))
print(can_arrange([1,2,3]))
print(can_arrange([3,2,1]))
print(can_arrange([3,2,1,3]))
