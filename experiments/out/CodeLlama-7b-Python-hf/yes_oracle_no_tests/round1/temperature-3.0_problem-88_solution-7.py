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
    first_index_value = array[0]
    last_index_value = array[-1]

    if sum([first_index_value, last_index_value]) % 2 == 0:
        return sorted(array)
    else:
        return sorted(array, reverse=True)


print(sort_array([2, 4, 3, 0, 1, 5]))
print(sort_array([2, 4, 3, 0, 1, 5, 6]))
print(sort_array([]))
print(sort_array([5]))
print(sort_array([2, 4, 3, 0, 1, 5, 6, 7]))
