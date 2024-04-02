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
    # check the sum of the first and last index
    if sum(array) % 2 == 0:
        # if the sum is even, sort the array in descending order
        array.sort(reverse=True)
    else:
        # if the sum is odd, sort the array in ascending order
        array.sort()
    return array


# test case 1
array = []
print(sort_array(array))  # correct output => []

# test case 2
array = [5]
print(sort_array(array))  # correct output => [5]

# test case 3
array = [2, 4, 3, 0, 1, 5]
print(sort_array(array))  # correct output => [0, 1, 2, 3, 4, 5]

# test case 4
array = [2, 4, 3, 0, 1, 5, 6]
print(sort_array(array))  # correct output => [6, 5, 4, 3, 2, 1, 0]
