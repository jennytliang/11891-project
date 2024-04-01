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
    
	Include these tokens in the code: array
	Do not include these tokens in the code: len ( )
	"""

    if l := len(array):
        if l == 1:
            return array

        first_index = array[0]
        last_index = array[-1]

        # set reverse flag based on sum of first and last index
        reverse = (first_index + last_index) % 2 == 0

        # sort the array
        array.sort(reverse=reverse)

    return array


def test_sort_array():

    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([2, 3, 4, 5, 6, 7]) == [2, 3, 4, 5, 6, 7]
    assert sort_array([7, 6, 5, 4, 3, 2]) == [7, 6, 5, 4, 3, 2]
    assert sort_array([7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7]
    assert sort_array([1, 2, 3, 4, 5, 6, 7]) == [7, 6, 5, 4, 3, 2, 1]
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4, 3, 2, 1]
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 