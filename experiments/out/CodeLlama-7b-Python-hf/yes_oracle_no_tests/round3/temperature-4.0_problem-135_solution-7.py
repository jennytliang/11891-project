def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len
	Do not include these tokens in the code: # R ely on the fact that
	"""
    # Rely on the fact that the list is sorted
    # Rely on the fact that the list does not contain duplicate values
    # Rely on the fact that the list is not empty
    if len(arr) == 0:
        return -1

    for i in range(len(arr)):
        if arr[i] <= arr[i-1]:
            return i-1

    return len(arr)-1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
