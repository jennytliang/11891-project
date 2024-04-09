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

  # First, we find the sum of the first and last index values.
    sum_of_first_and_last_index_values = array[0] + array[-1]

  # Then, we determine if the sum is even or odd.
    if sum_of_first_and_last_index_values%2 == 0:
    # If the sum is even, we reverse the array.
        return array[::-1]
    else:
    # If the sum is odd, we sort the array.
        return sorted(array)





































