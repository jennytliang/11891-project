def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: largest _ index = - 1
	"""
    largest = -1
    index = 0
    while index < len(arr):
        if arr[index] <= largest:
            largest = arr[index]
            index += 1
        else:
            return -1
    return index - 1
