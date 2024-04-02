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

  # find the sum of the first 2 index values
  #  2

  # if the sum of the two index values is even
  # 0, 5  even
  # 4, 1   even
  # 3, 0   odd
  # 3, 5   odd

  # sort the array ascending if the sum is odd,
  # or descending if the sum is even

  """
    First try, needless code, I overcomplicated things
    
    if len(array) < 1:
        return array

    array_sum = sum(array[0:2])

    if array_sum % 2 is 0:
      array.sort()
      return array
    else:
      array.sort(reverse=True)
      return array
  """

  # Solution (probably the cleanest and best)
  return_array = array
  array_sum = sum(array[:2]) % 2

  if array_sum == 0:
    return_array = sorted(return_array)
  else:
    return_array.sort(reverse=True)
  return return_array


# Elegant Solution, 3 lines
def sort_arrayB(array):
    return sorted(array, reverse = sum(array[:2]) % 2)
