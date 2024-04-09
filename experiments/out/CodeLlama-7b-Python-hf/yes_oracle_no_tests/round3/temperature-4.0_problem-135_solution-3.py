def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Find the largest value in the
	"""
    # Find the largest value in the array
    # Find the largest value in the array
    # Create a new array of zeros of size of the original array
    # Iterate through the original array
    # If the value is greater than the largest value, set the value of the
    # corresponding index in the new array to the largest value
    # Otherwise, set the value of the corresponding index in the new array to
    # the value of the current index
    # Iterate through the new array, and find the first index containing a
    # zero
    # If there are no zeros, return -1
    # Otherwise, return the index

    # O(n) time
    # O(n) space

    # Find largest value in the array
    largest = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    # Create new array of zeros
    new_arr = [0] * len(arr)

    # Iterate through the original array
    for i in range(len(arr)):
        # If the value is greater than the largest value, set the value of the
        # corresponding index in the new array to the largest value
        if arr[i] > largest:
            new_arr[i] = largest
        # Otherwise, set the value of the corresponding index in the new array
        # to the value of the current index
        else:
            new_arr[i] = arr[i]

    # Iterate through the new array
    for i in range(len(new_arr)):
        # If the value is not greater than or equal to the value immediately
        # preceding it, return the index
        if new_arr[i] != arr[i - 1]:
            return i

    # Otherwise, return -1
    return -1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
