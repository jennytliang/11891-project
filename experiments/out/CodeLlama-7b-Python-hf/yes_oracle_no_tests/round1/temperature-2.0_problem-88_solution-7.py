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

  # sort the array
  array.sort()

  # get the sum of the first and last index
  sum = array[0] + array[len(array) - 1]

  # if the sum is even, sort in descending order
  if sum % 2 == 0:
    # reverse the array
    array.reverse()

  return array

# print(sort_array([1, 2, 3, 4, 5, 6]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([0, 2, 4, 3, 1, 5]))
# print(sort_array([5, 7, 4, 2, 0, 1, 6]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 3, 2, 4, 6, 5]))
# print(sort_array([1, 