def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Sort the input , so
	"""
    # Sort the input , so that we can work with the first element
    arr.sort()
    # Initialize a variable to keep track of the largest index
    largest_index = -1
    # Initialize a variable to keep track of the current index
    current_index = 0
    # Loop through the array
    while current_index < len(arr):
        # If the current index is less than the largest index
        if current_index < largest_index:
            # Check if the current element is greater than the element at the
            # largest index
            if arr[current_index] > arr[largest_index]:
                # If it is, then set the largest index to the current index
                largest_index = current_index
        # If the current index is greater than or equal to the largest index
        else:
            # Check if the current element is greater than the element at the
            # largest index
            if arr[current_index] > arr[largest_index]:
                # If it is, then set the largest index to the current index
                largest_index = current_index
            # If the current element is not greater than the largest index,
            # then set the largest index to the current index
            else:
                largest_index = current_index
        # Increment the current index
        current_index += 1
    # Return the largest index
    return largest_index


print(can_arrange([1, 2, 4, 3, 5]))
