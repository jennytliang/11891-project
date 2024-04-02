def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: count = 0 #
	"""
    


def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
    Do not include these tokens in the code:
    count = 0 #
    token:
    arr
    smallest_change(arr) < 4:
    any_element(arr) == any_element(arr[::-1]):
    
    Examples
    smallest_change([1,2,3,5,4,7,9,6])
    4
    smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
    0
    smallest_change([1, 2, 3, 4, 3, 2, 2])
    1
    """
    arr2 = arr[::-1]
    arr3 = arr
    total = 0
    
    for v in range(0, len(arr)):
        if arr[v] != arr2[v]:
            for j in range(v + 1, len(arr)):
                if arr[j] == arr2[j]:
                    return j - v
                    
    return 0