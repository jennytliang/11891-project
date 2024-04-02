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
    
	Include these tokens in the code: if array == [] : return
	Do not include these tokens in the code: sorted _ =
	"""
    # First, sort the array in ascending order, then reverse the array.
    array.sort()
    array.reverse()
    return array


def sort_array_in_place(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array_in_place([]) => []
    * sort_array_in_place([5]) => [5]
    * sort_array_in_place([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array_in_place([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    
    Include these tokens in the code: if array == [] : return
	Do not include these tokens in the code: sorted _ =
    """
    # First, sort the array in ascending order, then reverse the array.
    array.sort()
    array.reverse()
    return array


def sort_array_with_count_even_odd(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array_with_count_even_odd([]) => []
    * sort_array_with_count_even_odd([5]) => [5]
   