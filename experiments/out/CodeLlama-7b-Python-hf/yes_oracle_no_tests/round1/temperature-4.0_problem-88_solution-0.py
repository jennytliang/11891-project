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
	"""
    # Check to see if the array is empty
    if array == []:
        return []
    # If the array is not empty, then we need to check to see if the sum of the first and last value is even or odd
    if sum(array[0], array[-1]) % 2 == 0:
        # If the sum of the first and last value is even, then we need to sort the array in descending order
        # We can use the sorted function to return a new sorted array
        return sorted(array, reverse=True)
    else:
        # If the sum of the first and last value is odd, then we need to sort the array in ascending order
        # We can use the sorted function to return a new sorted array
        return sorted(array)

















