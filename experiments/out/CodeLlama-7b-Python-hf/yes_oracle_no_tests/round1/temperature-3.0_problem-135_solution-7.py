def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len ( arr ) -
	"""
    # Initialize the largest index of an element which is not greater than or
    # equal to the element immediately preceding it.
    index = -1
    # Iterate through the array.
    for i in range(len(arr)):
        # If the element is greater than or equal to the element immediately
        # preceding it.
        if arr[i] >= arr[i - 1]:
            # Set the largest index of an element which is not greater than or
            # equal to the element immediately preceding it.
            index = i - 1
    # Return the largest index of an element which is not greater than or equal
    # to the element immediately preceding it.
    return index


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
