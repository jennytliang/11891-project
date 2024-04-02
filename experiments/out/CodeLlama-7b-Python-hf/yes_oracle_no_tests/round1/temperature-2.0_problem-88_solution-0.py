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
	Do not include these tokens in the code: len ( )
	"""

 
    # Write your code here.
    # Add your function below this row 
    
    if len(array) == 0:
        return []
    
    if len(array) == 1:
        return array
    
    if sum(array[0:2]) % 2 == 0:
        return sorted(array)
    else:
        return sorted(array, reverse=True)
    
    # Do not change the code below 
    return array
    

# Write your function here
def sort_array(array):
    '''
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
	Do not include these tokens in the code: len ( )
	'''

    # Write your code here.
    # Add your function below this row 
    
    if len(array) == 0:
        return []
    
    if len(array) == 1:
        return array
    
    if sum(array[0:2]) % 2 == 0:
        return sorted(array)
    else:
        return sorted(array, reverse=True)
    
    # Do not change the code below 
    return array

# Do not remove the lines below.
# do not change the indentation of the code