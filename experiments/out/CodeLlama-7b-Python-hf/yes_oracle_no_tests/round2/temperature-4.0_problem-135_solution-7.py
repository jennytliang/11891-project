def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: arr . sort ()
	"""
    # Rely on the fact that the array is sorted
    # and that the array does not contain duplicate values.
    # Start at the first element.
    # If the next element is greater than or equal to the current element,
    # we have not found the largest index.
    # Otherwise, we have found the largest index.
    # Check the next element.
    largest_index = -1
    current_index = 0
    while current_index < len(arr) - 1:
        if arr[current_index + 1] >= arr[current_index]:
            largest_index = current_index
            current_index += 1
        else:
            break
    return largest_index


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
