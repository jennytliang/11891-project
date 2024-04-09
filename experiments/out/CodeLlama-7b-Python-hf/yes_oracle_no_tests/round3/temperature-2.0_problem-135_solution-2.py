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
    # create a dictionary with the key as the value and the value as the
    # index of the value
    index_dict = {}
    for i in range(len(arr)):
        if arr[i] not in index_dict:
            index_dict[arr[i]] = i
    # create a sorted list of the keys
    sorted_keys = sorted(index_dict.keys())
    # iterate over the sorted list in reverse order
    for i in range(len(sorted_keys) - 1, -1, -1):
        # if the value is not greater than or equal to the value preceding it
        if sorted_keys[i] < sorted_keys[i-1]:
            # return the index of the sorted key
            return index_dict[sorted_keys[i]]
    # otherwise return -1
    return -1
