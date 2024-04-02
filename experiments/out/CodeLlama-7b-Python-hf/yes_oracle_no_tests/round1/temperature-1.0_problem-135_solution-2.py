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
    
    # Iterate through the array, keeping track of the current highest value
    # and the current index.
    highest, index = 0, 0
    for i in range(len(arr)):
        if arr[i] > highest:
            highest = arr[i]
            index = i

    # If the current highest value is not equal to the last value, return -1.
    if arr[len(arr) - 1] != highest:
        return -1

    # Iterate through the array again, comparing the current value to the
    # highest value.
    for i in range(len(arr)):
        if arr[i] < highest:
            return i

    return -1
