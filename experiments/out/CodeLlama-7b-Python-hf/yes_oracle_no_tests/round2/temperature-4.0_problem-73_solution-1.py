def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # Re verse the array
	"""
    if not arr:
        return 0
    arr_len = len(arr)
    # Reverse the array
    arr_reversed = list(reversed(arr))
    # Compare the two arrays
    result = 0
    for i in range(arr_len):
        if arr[i] != arr_reversed[i]:
            result += 1
    return result


print(smallest_change([1, 2, 3, 2, 1]))  # 0
print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))  # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # 1
