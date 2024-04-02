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
    # Find the index of the maximum element in the input array.
    # If the maximum element is less than the minimum element,
    # return -1.
    max_element = max(arr)
    min_element = min(arr)
    if max_element < min_element:
        return -1

    # Find the index of the minimum element in the input array.
    # If the minimum element is greater than the maximum element,
    # return -1.
    min_element_index = arr.index(min_element)
    if min_element > max_element:
        return -1

    # If the difference between the indices of the minimum element
    # and the maximum element is one, return the index of the
    # maximum element.
    if max_element - min_element_index == 1:
        return arr.index(max_element)

    # If the difference between the indices of the minimum element
    # and the maximum element is greater than one, return the index
    # of the minimum element.
    if max_element - min_element_index > 1:
        return min_element_index

    # If the difference between the indices of the minimum element
    # and the maximum element is less than one, return -1.
    if max_element - min_element_index < 1:
        return -1


print(can_arrange([1,2,4,3,5]))
print(can_arrange([1,2,3]))
