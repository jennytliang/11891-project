def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code:  if len ( arr ) ==  0 :
	"""

    # for each element in the array, find the index of the last element which is
    # less than or equal to it
    for i in range(len(arr)):
        if arr[i] > arr[i-1]:
            # if the previous element is greater than the current element then
            # there is no index which is less than or equal to it
            return -1
        else:
            # find the index of the last element which is less than or equal to
            # the current element
            for j in range(i-1, -1, -1):
                if arr[j] <= arr[i]:
                    return j


# test function
def test_can_arrange():
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 3]) == -1
    assert can_arrange([1, 2, 3, 4, 5]) == -1
    assert can_arrange([5, 4, 3, 2, 1]) == -1
    assert can_arrange([1, 3, 4, 5, 2]) == 2
    assert can_arrange([1, 2, 3, 4, 5]) == -1
    assert can_arrange([1, 2, 3, 5, 4]) == 3
    assert can_arrange([1, 3, 4, 2, 5]) == 2
    assert can_arrange([1, 2, 3, 5, 4]) == 3
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 3, 5, 4]) == 3
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 4, 3,