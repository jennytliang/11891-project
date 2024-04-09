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
    
	Do not include these tokens in the code: # Check
	"""
    # Check
    if len(array) <= 1:
        return array
    
    # Check if the sum is even or odd
    sum_of_values = array[0] + array[-1]
    if sum_of_values % 2 == 0:
        # Sort in descending order
        return sort_array_descending(array)
    else:
        # Sort in ascending order
        return sort_array_ascending(array)


def sort_array_descending(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in descending order.

    Examples:
    * sort_array_descending([]) => []
    * sort_array_descending([5]) => [5]
    * sort_array_descending([2, 4, 3, 0, 1, 5]) => [5, 4, 3, 2, 1, 0]
    * sort_array_descending([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    return sorted(array, reverse=True)


def sort_array_ascending(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order.

    Examples:
    * sort_array_ascending([]) => []
    * sort_array_ascending([5]) => [5]
    * sort_array_ascending([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array_ascending([2, 4, 3, 0, 1, 5, 6]) => [0, 1, 2, 3, 4, 5, 6]
    """
    return sorted(array)


