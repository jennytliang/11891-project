def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code:  if len ( arr ) ==  0 :
	"""

    # A list of the indices of the elements that can be the largest, in order.
    largest_indices = []

    # The largest element seen so far.
    largest_element = -1

    # The largest index of the largest element seen so far.
    largest_index = -1

    # The largest index seen so far.
    largest_index_seen = -1

    # Iterate through the array.
    for index, element in enumerate(arr):

        # If the element is larger than the largest element seen so far,
        # update the largest element and largest index seen so far.
        if element > largest_element:
            largest_element = element
            largest_index_seen = index

        # If the element is equal to the largest element seen so far and
        # its index is larger than the largest index seen so far, update
        # the largest index seen so far.
        elif element == largest_element and index > largest_index_seen:
            largest_index_seen = index

        # If the element is equal to the largest element seen so far and
        # its index is equal to the largest index seen so far, add the
        # index to the list of indices.
        elif element == largest_element and index == largest_index_seen:
            largest_indices.append(index)

    # If the largest index seen so far is equal to the last index in the
    # array, return -1.
    if largest_index_seen == len(arr) - 1:
        return -1

    # Otherwise, return the index of the largest element.
    return largest_index_seen
