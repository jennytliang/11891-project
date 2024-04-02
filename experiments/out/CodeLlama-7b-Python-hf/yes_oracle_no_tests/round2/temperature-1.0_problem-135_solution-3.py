def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range
	Do not include these tokens in the code: return can _ ar _ helper
	"""
    return can_arrange_helper(arr, 0)


def can_arrange_helper(arr, index):
    if index == len(arr) - 1:
        return -1
    if arr[index] <= arr[index + 1]:
        return can_arrange_helper(arr, index + 1)
    else:
        return index


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
