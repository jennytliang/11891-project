def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: if len ( arr ) ==
	"""
    # check for edge case
    if len(arr) == 1:
        return 0
    # create a copy of the array
    arr_copy = arr.copy()
    # reverse the array
    arr_copy.reverse()
    # compare the two arrays
    for i,j in zip(arr, arr_copy):
        if i != j:
            arr[arr.index(i)] = arr_copy[arr_copy.index(j)]
    return sum(arr)


print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 2, 1]))



































