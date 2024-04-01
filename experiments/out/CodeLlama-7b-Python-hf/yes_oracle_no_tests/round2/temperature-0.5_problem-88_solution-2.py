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
    # Checking if the array is empty
    if not array:
        return []
    
    # Checking if the sum of the first and last index is even
    if (array[0] + array[-1]) % 2 == 0:
        # If even, sort in descending order
        return sorted(array, reverse=True)
    else:
        # If odd, sort in ascending order
        return sorted(array)


if __name__ == '__main__':
    print(sort_array([2, 4, 3, 0, 1, 5, 6]))
