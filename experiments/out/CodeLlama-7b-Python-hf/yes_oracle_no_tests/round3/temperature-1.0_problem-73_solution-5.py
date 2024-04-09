def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # find the middle of the array
	"""
    # check for trivial cases
    if len(arr) < 2:
        return 0

    # create a mirrored copy of the array
    mirrored_arr = arr[:]
    mirrored_arr.reverse()

    # create a copy of the array with all duplicate elements removed
    unique_arr = []
    for element in arr:
        if element not in unique_arr:
            unique_arr.append(element)

    # find all elements in the mirrored copy that are not in the unique copy
    mirrored_diff = []
    for element in mirrored_arr:
        if element not in unique_arr:
            mirrored_diff.append(element)

    # find all elements in the unique copy that are not in the mirrored copy
    unique_diff = []
    for element in unique_arr:
        if element not in mirrored_arr:
            unique_diff.append(element)

    # return the minimum of the two
    return min(len(mirrored_diff), len(unique_diff))


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
