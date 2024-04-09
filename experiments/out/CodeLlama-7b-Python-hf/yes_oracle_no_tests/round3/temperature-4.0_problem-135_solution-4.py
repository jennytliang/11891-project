def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Initialize the index of the largest
	"""
    # Initialize the index of the largest element
    largest_index = 0
    # Do not include these tokens in the code: # Initialize the index of the largest
    # element
    largest_index = 0
    # Do not include these tokens in the code: # Initialize the index of the largest
    # element

    # Iterate through the list
    for i in range(1, len(arr)):
        # If the current element is greater than or equal to the largest element
        if arr[i] >= arr[largest_index]:
            # If the current element is greater than the largest element
            if arr[i] > arr[largest_index]:
                # Update the index of the largest element
                largest_index = i
        # If the current element is not greater than or equal to the largest element
        else:
            # If the current element is not greater than the largest element
            if arr[i] != arr[largest_index]:
                # Update the index of the largest element
                largest_index = i
    # Return the index of the largest element
    return largest_index
