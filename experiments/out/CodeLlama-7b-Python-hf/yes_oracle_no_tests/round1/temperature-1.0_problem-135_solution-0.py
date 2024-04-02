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
    # Find the largest element in the array
    max_val = max(arr)
    # Create a new array with the same length as the original
    new_arr = [None] * len(arr)
    # Iterate over the original array
    for i in range(len(arr)):
        # Find the index of the element which is not greater than or equal to
        # the element immediately preceding it
        j = i - 1
        while j >= 0 and arr[j] >= arr[i]:
            j -= 1
        # If no such element exists return -1
        if j < 0:
            return -1
        # Otherwise assign the element at the index to the element at i
        new_arr[i] = arr[j]
    # Return the index of the last element
    return len(arr) - 1
