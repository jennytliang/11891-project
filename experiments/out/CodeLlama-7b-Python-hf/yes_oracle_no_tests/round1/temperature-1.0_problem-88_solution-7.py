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

  arr = list(array)

  def sort_(array, direction=True):

      if not array or len(array) == 1:
          return array

      if (array[-1] + array[0]) % 2:
          return array

      array.sort() if direction else array.sort(reverse=True)

      return sort_(array[:-1], not direction) + [array[-1]]

  print(arr)
  sorted_arr = sort_(arr)

  return sorted_arr

