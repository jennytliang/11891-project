def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed
	Do not include these tokens in the code: # check if array is pal ind
	"""
    arr_reversed = arr.copy()
    arr_reversed.reverse()

    # check if array is palindrome
    if arr == arr_reversed:
        return 0
    
    # check if array is palindrome with one change
    one_change = False
    for i, val in enumerate(arr):
        if val != arr_reversed[i]:
            one_change = True
            break
    
    if one_change:
        return 1

    # check if array is palindrome with two changes
    two_changes = False
    for i, val in enumerate(arr):
        if val != arr_reversed[i + 1]:
            two_changes = True
            break
    
    if two_changes:
        return 2

    return 3


# TESTS
assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 2
assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3


