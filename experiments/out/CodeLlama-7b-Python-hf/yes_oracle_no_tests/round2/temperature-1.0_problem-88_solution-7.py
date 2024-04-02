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
	Do not include these tokens in the code: # Find the sum of the
	"""
    pass


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(sort_array([0, 1, 2, 3, 4, 5])) == [0, 1, 2, 3, 4, 5], "Sorted"
    assert list(sort_array([5, 4, 3, 2, 1])) == [1, 2, 3, 4, 5], "Reversed"
    assert list(sort_array([5, 3, 2])) == [2, 3, 5], "Edge-1"
    assert list(sort_array([5, -1, -10, 9, -2])) == [-10, -2, -1, 5, 9], "Negatives"
    assert list(sort_array([0, 0, 0, 0, 0])) == [0, 0, 0, 0, 0], "All zeros"
    assert list(sort_array([1, 1, 1, 1, 1])) == [1, 1, 1, 1, 1], "All ones"
    assert list(sort_array([1, 2, 3, 5, 6, 7, 9, 0, 0, 0])) == [0, 0, 0, 1, 2, 3, 5, 6, 7, 9], "Sorted"
