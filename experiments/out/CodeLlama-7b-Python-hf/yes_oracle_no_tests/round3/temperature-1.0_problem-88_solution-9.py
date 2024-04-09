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
    
	Do not include these tokens in the code: not
	"""


    first_index_value = array[0]
    last_index_value = array[-1]

    sum_of_first_and_last_index_values = first_index_value + last_index_value

    if sum_of_first_and_last_index_values % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)


def sort_array_with_zip(array):
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
    
	Do not include these tokens in the code: not
	"""


    first_index_value = array[0]
    last_index_value = array[-1]

    sum_of_first_and_last_index_values = first_index_value + last_index_value

    if sum_of_first_and_last_index_values % 2 == 1:
        return [*zip(*sorted(zip(array)))]
    else:
        return [*zip(*sorted(zip(array), reverse=True))]


def sort_array_using_tuple_assignment(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort