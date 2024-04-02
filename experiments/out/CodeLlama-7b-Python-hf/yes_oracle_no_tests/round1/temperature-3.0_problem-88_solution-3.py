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
    # First, we will check the sum of the first and last index values to determine if we need to sort in ascending or descending order.
    # Then we will add the first or last index value to a new array depending on the order that is needed.
    # Then we will iterate through the array and add the index values to the new array.
    # Finally, we will return the new array.

    # First, we will check the sum of the first and last index values to determine if we need to sort in ascending or descending order.
    if array == []:
        return array
    # Then we will add the first or last index value to a new array depending on the order that is needed.
    sum_of_first_and_last_index_values = array[0] + array[-1]
    # Then we will iterate through the array and add the index values to the new array.
    if sum_of_first_and_last_index_values % 2 == 0:
        new_array = []
        for index in range(len(array)):
            new_array.append(array[-1 - index])
    else:
        new_array = []
        for index in range(len(array)):
            new_array.append(array[index])
    # Finally, we will return the new array.
    return new_array

# Test cases
print(sort_array([2, 4, 3, 0, 1, 5])) # [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6])) # [6, 5, 4, 3, 2, 1, 0]
print(sort_array([])) # []
print(sort_array([5])) # [5]
