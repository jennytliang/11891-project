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

  # If array is empty or has only one element, return the array
  if len(array) == 0 or len(array) == 1:
    return array

  # Calculate the sum of the first and last index values
  # If sum is even, sort in descending order
  # If sum is odd, sort in ascending order
  if array[0] + array[-1] % 2 == 0:
    # Sort in ascending order
    sorted_array = sorted(array)
  else:
    # Sort in descending order
    sorted_array = sorted(array, reverse = True)

  return sorted_array


def sort_array_two(array):
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

  # If array is empty or has only one element, return the array
  if len(array) == 0 or len(array) == 1:
    return array

  # Calculate the sum of the first and last index values
  # If sum is even, sort in ascending order
  # If sum is odd, sort in descending order
  sum = array[0] + array[-1]
  if sum