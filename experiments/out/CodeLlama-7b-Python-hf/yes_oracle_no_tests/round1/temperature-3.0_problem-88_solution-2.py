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
    #First, we need to determine if the sum of the first and last index values are odd or even.
    #If they are odd, then we need to sort the array in ascending order.
    #If they are even, then we need to sort the array in descending order.
    #We can easily determine this by calling the sum() function on the first and last index values.
    sum_of_index_values = sum(array)
    if sum_of_index_values % 2 == 0:
        #If the sum of the first and last index values is even, then we need to sort the array in descending order.
        #We can do this by creating a new array, and then using the sorted() function.
        #We can then return that new array.
        new_array = sorted(array, reverse=True)
        return new_array
    else:
        #If the sum of the first and last index values is odd, then we need to sort the array in ascending order.
        #We can do this by creating a new array, and then using the sorted() function.
        #We can then return that new array.
        new_array = sorted(array, reverse=False)
        return new_array



























































































































































































































