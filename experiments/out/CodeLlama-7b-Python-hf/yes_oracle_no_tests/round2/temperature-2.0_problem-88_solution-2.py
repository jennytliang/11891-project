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
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # 1 . get the
	"""
    if not array:
        return array

    result = []
    if sum(array[0:2]) % 2 == 0:
        for i in range(len(array)):
            result.append(min(array))
            array.remove(min(array))
    else:
        for i in range(len(array)):
            result.append(max(array))
            array.remove(max(array))
    return result


def test_sort_array():
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort_array([1, 3, 2, 4, 5]) == [1, 3, 2, 4, 5]
    assert sort_array([1, 2, 4, 3, 5]) == [1, 2, 4, 3, 5]
    assert sort_array([1, 2, 5, 4, 3]) == [1, 2, 5, 4, 3]
    assert sort_array([1, 4, 2, 3, 5]) == [1, 4, 2, 3, 5]
    assert sort_array([1, 4, 3, 2, 5]) == [1, 4, 3, 2, 5]
    assert sort_array([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    assert sort_array([5, 4, 