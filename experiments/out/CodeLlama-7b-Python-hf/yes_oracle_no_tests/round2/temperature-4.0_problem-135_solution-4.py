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
    # Initialize the index of the largest element in the array to -1
    largest_index = -1
    # Initialize the largest element in the array to -1
    largest = -1
    # Iterate over the array backwards
    for i in range(len(arr) - 1, -1, -1):
        # If the current element in the array is greater than or equal to the
        # largest element then update the largest and largest index
        if arr[i] >= largest:
            largest = arr[i]
            largest_index = i
    # If the largest index is -1 then return -1
    if largest_index == -1:
        return -1
    # If the largest index is not -1 then iterate over the array
    for i in range(len(arr)):
        # If the current element in the array is greater than or equal to the
        # largest element then return -1
        if arr[i] >= largest:
            return -1
        # If the current element in the array is less than the largest element
        # and the current element is greater than the element at the largest
        # index then update the largest index
        if arr[i] < largest and i < largest_index:
            largest_index = i
    # Return the largest index
    return largest_index
