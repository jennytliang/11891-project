def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # Find the middle element of the
	"""
    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 0 if arr[0] == arr[1] else 1
    if len(arr) == 3:
        return 0 if arr[0] == arr[2] else 1

    mid = len(arr) // 2

    if arr[mid] == arr[mid - 1]:
        return smallest_change(arr[:mid - 1] + arr[mid + 1:])
    if arr[mid] == arr[mid + 1]:
        return smallest_change(arr[:mid] + arr[mid + 2:])
    return 1 + min(smallest_change(arr[:mid]), smallest_change(arr[mid:]))


def smallest_change_2(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # Find the middle element of the
	"""
    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 0 if arr[0] == arr[1] else 1
    if len(arr) == 3:
        return 0 if arr[0] == arr[2] else 1

    mid = len(arr) // 2

    if arr[mid] == arr[mid - 1]:
        return