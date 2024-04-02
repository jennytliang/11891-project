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
    
	Include these tokens in the code: return []
	"""


  if array == []:
    return []
  elif len(array) == 1:
    return array
  
  l = len(array)

  sorted_array = []
  # loop thru index 0 to (l-2) --> (4-2) = len of half the array length
  for i in range (0, l-1, 1):
    even_odd = 0

    if (array[0] + array[-1]) % 2 == 0:
      even_odd = 1
    
    midpoint = l // 2

    sorted_array_1 = []
    sorted_array_2 = []

    for j in range(0, l, 1):
      if j < midpoint:
        sorted_array_1.append(array[j])
      else:
        sorted_array_2.append(array[j])

    if sorted_array_1[0] > sorted_array_2[0]:
      sorted_array.append(sorted_array_1[0])
      sorted_array.append(sorted_array_2[0])
      length = len(sorted_array_2)
      for k in range (1, length, 1):
        sorted_array.append(sorted_array_2[k])
        sorted_array.append(sorted_array_1[k])
    
    elif sorted_array_1[0] < sorted_array_2[0]:
      sorted_array.append(sorted_array_2[0])
      sorted_array.append(sorted_array_1[0])
      length = len(sorted_array_2)
      for k in range (1, length, 1):
        sorted_array.append(sorted_array_1[k])
        sorted_array.append(sorted_array_2[k])
    
    else:
      sorted_array = []
      l -= 1
      sorted_array = array

  return sorted_array
  
  
def solution_sort_array(array):
  print(array)
  
  # sort and return
  if (array[0] + array[-