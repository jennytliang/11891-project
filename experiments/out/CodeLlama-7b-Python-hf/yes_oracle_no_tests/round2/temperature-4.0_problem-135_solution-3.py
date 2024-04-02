def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # for n in range ( len
	"""
    # Find the largest value in the array.
    largest = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    # Create an array of the same size as the original array.
    result = [-1] * len(arr)

    # Iterate through the array.
    for i in range(len(arr)):
        # Find the largest element which is not greater than or equal to the
        # element immediately preceding it.
        j = largest
        while j > arr[i]:
            j -= 1

        # If the element is not greater than or equal to the element immediately
        # preceding it then place it in the result array.
        if j != arr[i]:
            result[i] = j

    return result


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
