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
    
	Do not include these tokens in the code: # First , we will check the
	"""
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return array
    elif len(array) == 2:
        return [min(array), max(array)]
    else:
        sum_array = sum(array[0:2])
        if sum_array % 2 == 0:
            return array[::-1]
        else:
            return array
