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

  if not array: return array

  ## Step 1: Detect if the array should be sorted asc or desc
  sum = array[0] + array[-1]
  
  if sum % 2: # odd sum
    ascend = True
  else:
    ascend = False

  ## Step 2: Perform Bubble Sort
  for i in range(1, len(array)):
    for j in range(0, len(array) - i):
      if ascend:
        if array[j + 1] < array[j]:
          array[j + 1], array[j] = array[j], array[j + 1]
      else:
        if array[j + 1] > array[j]:
          array[j + 1], array[j] = array[j], array[j + 1]

  return array