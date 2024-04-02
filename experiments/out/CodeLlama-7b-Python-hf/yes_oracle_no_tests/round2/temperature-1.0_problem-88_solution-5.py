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
    
	Include these tokens in the code: if array == [] : return []
	Do not include these tokens in the code: # Your code here
	"""
    return sorted(array, key=lambda x: x * 2) if sum(array) % 2 == 0 else sorted(array, key=lambda x: x * 2, reverse=True)


def test_sort_array():
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert sort_array([2, 2, 2, 2]) == [2, 2, 2, 2]
    assert sort_array([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort_array([2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert sort_array([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort_array([5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_array([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6,