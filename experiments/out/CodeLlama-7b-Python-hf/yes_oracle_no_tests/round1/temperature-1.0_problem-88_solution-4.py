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

  if array == []:
    return array
  else:
    even = []
    odd = []
    for i in array:
      if i%2 == 0:
        even.append(i)
      else:
        odd.append(i)
    if len(even)*len(odd) == 0:
      return array 
      
    even_sorted = sorted(even, reverse=len(even)%2)
    odd_sorted = sorted(odd, reverse=(len(odd)%2 - 1))
    if len(even_sorted+odd_sorted)%2 == 0:
      even_sorted.insert(0, odd_sorted[0])
      even_sorted.append(odd_sorted[1])
    else:
      even_sorted.insert(0, odd_sorted[0])
    
    return even_sorted + odd_sorted

assert sort_array([]) == []
assert sort_array([5]) == [5]
assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
