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
    # Check if array is empty
    if array == []:
        return array
    
    # Check the sum of the first and last index values
    if array[0] + array[-1] % 2 == 0:
        # Sort in ascending order
        array.sort()
    else:
        # Sort in descending order
        array.sort(reverse=True)
    
    return array


print(sort_array([2, 4, 3, 0, 1, 5]))
print(sort_array([2, 4, 3, 0, 1, 5, 6]))
print(sort_array([]))
print(sort_array([5]))
