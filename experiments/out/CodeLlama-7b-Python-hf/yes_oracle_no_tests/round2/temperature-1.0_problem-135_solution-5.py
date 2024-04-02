def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for
	Do not include these tokens in the code: # We maintain two pointers to
	"""

    # TODO: do this in one pass in time
    # TODO: do this in 1.5 * n space
    # If array is empty, return -1
    if not arr:
        return -1
    i = 1  # initial index value
    # Start with smallest value
    smallest = arr[0]
    # TODO: if index i isn't greater than or equal to
    # and value at i is greater than value at i-1
    # then swap i-1 and i values
    while i < len(arr):
        if arr[i] >= arr[i-1]:
            smallest = min(arr[i],arr[i-1])
            arr[i-1] = smallest
            arr[i] = arr[i] + smallest
        i += 1


    # print(arr)
    # Traverse back and find largest preceding value
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i+1]:
            return i
        
    return arr.index(max(arr))


assert can_arrange([1,2,4,3,5]) == 3, "Should return 3"
assert can_arrange([1,2,3,4,5]) == 2, "Should return 2"
assert can_arrange([2,7,4,5,8]) == 3, "Should return 3"

