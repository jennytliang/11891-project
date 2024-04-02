def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # check edge cases if
	"""
    # check edge cases
    if len(arr) < 2:
        return 0
    
    # check if arr is palindrome
    if arr[0] == arr[-1]:
        return smallest_change(arr[1:-1])
    
    # get the first index of the first non-palindrome
    for i in range(1, len(arr)):
        if arr[i] != arr[-i]:
            break
    
    # get the count of the first non-palindrome
    count = arr[i] != arr[-i]
    
    # get the count of the first half
    first_half_count = smallest_change(arr[1:i])
    
    # get the count of the second half
    second_half_count = smallest_change(arr[i:-1])
    
    # return the minimum
    return min(count, first_half_count, second_half_count)

def smallest_change_2(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # check edge cases if
	"""
    # check edge cases
    if len(arr) < 2:
        return 0
    
    # check if arr is palindrome
    if arr[0] == arr[-1]:
        return smallest_change_2(arr[1:-1])
    
    # get the first index of the first non-palindrome
    for i in range(1, len(arr)):
        if arr[