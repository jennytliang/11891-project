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

  reverse = False
  if sum(array[0:2])*2 == sum(array):
    reverse = True
  array = sorted(array, reverse=reverse)
  return array


### Testing ###

sort_array_tests = [
  ( [], [] ),
  ( [5], [5] ),
  ( [1], [1] ),
  ( [5, 4], [4, 5] ),  # sorted
  ( [1, -2], [-2, 1] ),  # sorted
  ( [5, 4, 3, 0, 1, 5], [0, 1, 2, 3, 4, 5] ),  # sorted
  ( [5, 20, 28, 1, 6, 8], [1, 5, 6, 8, 28, 20] ),  # sorted
  ( [5, 4, 10, 3, 0, 1, 5], [0, 1, 2, 3, 4, 5, 5] ),  # un-sorted
  ( [5, 10, 20, 4, 1, 6, 8], [1, 4, 5, 6, 8, 10, 20] ),  # un-sorted
  ( [5, 4, 10, 3, 0, 1, 5, 2], [0, 1, 2, 3, 4, 5, 5, 10] ),  # un-sorted
  ( [5, 4, 3, 0, 1, 3, 0], [0, 0, 1, 3, 3, 4, 5] ),  # sorted
  ( [5, 4, 3, 0, 1, 2, 0], [0, 0, 1, 2, 3, 4, 5] ),  # sorted
  ( [5, 4, 3, 0, 1, 3, 7