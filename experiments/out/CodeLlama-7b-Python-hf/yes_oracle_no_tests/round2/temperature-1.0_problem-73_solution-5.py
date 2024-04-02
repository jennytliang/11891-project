def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # find the middle of
	"""
    # find the middle of the array
    middle = len(arr) // 2
    # reverse the second half of the array
    arr[middle:] = arr[middle:][::-1]
    # count the number of differences
    return sum(arr[i] != arr[i+1] for i in range(len(arr)-1))


def test_smallest_change():
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 6, 5, 4, 7]) == 2
    assert smallest_change([1, 2, 3, 4, 5, 6, 7]) == 2
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8]) == 3
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 6
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 7
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 8
    assert smallest_change([1,