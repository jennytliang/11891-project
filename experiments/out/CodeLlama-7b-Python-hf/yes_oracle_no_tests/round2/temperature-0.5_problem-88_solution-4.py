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
	Do not include these tokens in the code: l := len ( )
	"""


    def sort_array_helper(array):
        """
        Helper function to sort an array.
        """
        # sort the array in ascending order if the sum( first index value, last index value) is odd,
        # or sort it in descending order if the sum( first index value, last index value) is even.
        if sum(array) % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)


    # sort the array and return it.
    return sort_array_helper(array)



print(sort_array([2, 4, 3, 0, 1, 5, 6]))
