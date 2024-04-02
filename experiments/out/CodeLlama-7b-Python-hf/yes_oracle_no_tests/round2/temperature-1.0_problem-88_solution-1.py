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
	Do not include these tokens in the code: # sort the
	"""
    # My Implementation
    # Step 1: check if the sum is odd or even
    sum_array = array[0] + array[-1]
    # Step 2: define the sort_type
    if sum_array % 2 == 0:
        sort_type = True
    else:
        sort_type = False
    # Step 3: sort the array
    array.sort(reverse=sort_type)
    return array


def sort_array_two(array):
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
	Do not include these tokens in the code: # sort the
	"""
    # My Implementation
    # Step 1: check if the sum is odd or even
    sum_array = array[0] + array[-1]
    # Step 2: define the sort_type
    if sum_array % 2 == 0:
        sort_type = False
    else:
        sort_type = True
    # Step 3: sort the array
    array.sort(reverse=sort_type)
    return array


def sort_array_three(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
