def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed , c nt = arr
	"""
    cnt = 0
    re = arr[::-1]
    for i in range(len(arr)):
        if(arr[i] != re[i]):
            cnt += 1
    return cnt


def test_smallest_change():
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 2
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 3
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 4
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 5
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 6
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,