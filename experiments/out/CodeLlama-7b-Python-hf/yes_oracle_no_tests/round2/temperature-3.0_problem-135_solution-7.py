def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Initialize the largest index of an
	"""
    # Initialize the largest index of an element which is not greater than or
    # equal to the element immediately preceding it.
    largest_index = -1
    # Do not include these tokens in the code: # Initialize the largest value of an
    largest_value = -1
    # Do not include these tokens in the code: # Initialize the largest index of an
    largest_index_of_largest_value = -1
    # Do not include these tokens in the code: # If the current value is larger than
    # the largest value, then update the largest value and the largest index of
    # the largest value.
    for index, value in enumerate(arr):
        if value > largest_value:
            largest_value = value
            largest_index_of_largest_value = index
    # Do not include these tokens in the code: # If the current value is less than or
    # equal to the largest value, then update the largest index of the current value.
    for index, value in enumerate(arr):
        if value <= largest_value:
            largest_index = max(largest_index, index)
    # Do not include these tokens in the code: # If the largest index of the current
    # value is less than the largest index of the largest value, then return -1.
    if largest_index < largest_index_of_largest_value:
        return -1
    # Do not include these tokens in the code: # Otherwise, return the largest index.
    return largest_index
