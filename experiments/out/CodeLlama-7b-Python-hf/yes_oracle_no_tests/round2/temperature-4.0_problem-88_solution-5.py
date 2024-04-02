def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    
	Do not include these tokens in the code: # check for empty array
	"""
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    if len(array) == 2:
        if (array[0] + array[1]) % 2 == 0:
            return [array[1], array[0]]
        else:
            return array
    if len(array) == 3:
        if (array[0] + array[2]) % 2 == 0:
            return [array[2], array[1], array[0]]
        else:
            return [array[0], array[1], array[2]]

    if (array[0] + array[-1]) % 2 == 0:
        return sort_array(array[1:-1]) + [array[0], array[-1]]
    else:
        return sort_array(array[1:-1]) + [array[-1], array[0]]


def test_sort_array():
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([2, 4, 3, 0, 1, 5, 6, 7]) == [6, 5, 4, 3, 2, 1, 0, 7]
    assert sort_array([2, 4, 3, 0, 1, 5, 6, 7, 8]) == [8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert sort_array([2, 4, 3, 0, 1, 5, 6, 7, 8, 9]) == [9, 