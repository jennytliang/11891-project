def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Create a dictionary of index
	"""
    if len(arr) <= 1:
        return -1
    result = {}
    for i in range(len(arr)):
        result[arr[i]] = i
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1] and result[arr[i]] == i:
            return i - 1
    return -1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
print(can_arrange([5, 4, 3, 2, 1]))
print(can_arrange([1, 2, 3, 3, 4]))
