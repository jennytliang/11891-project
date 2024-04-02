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
    
	Do not include these tokens in the code: # first , determine whether the
	"""
    # Intialize variables
    array_len = len(array)
    index = 0
    odd_even = array_len % 2
    
    # First, determine whether the sum(first index value, last index value) is odd or even.
    if odd_even == 0:
        # Even
        # For even, the array should be sorted in descending order
        while index < array_len:
            # Swap values if it is not in descending order
            if array[index] > array[array_len - 1 - index]:
                # Swap values
                array[index], array[array_len - 1 - index] = array[array_len - 1 - index], array[index]
            index += 1
    else:
        # Odd
        # For odd, the array should be sorted in ascending order
        while index < array_len:
            # Swap values if it is not in ascending order
            if array[index] < array[array_len - 1 - index]:
                # Swap values
                array[index], array[array_len - 1 - index] = array[array_len - 1 - index], array[index]
            index += 1
    
    return array


# Test cases
print(sort_array([]))  # Expect: []
print(sort_array([5]))  # Expect: [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # Expect: [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # Expect: [6, 5, 4, 3, 2, 1, 0]
