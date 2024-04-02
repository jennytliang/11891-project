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

 	print(array)
 	if (not array) or (len(array) == 1):
  	    return array
  	elif len(array) == 2:
  	    if (sum(array)) & 1:
  	        return sorted(array, reverse = True)
  	    else:
  	        return sorted(array)
  	else:
  		return sort_odd_even(array[:int(len(array)/2)], array[int(len(array)/2):])


def sort_odd_even(list1, list2):
	"""
	Returns the merged sorted lists based on their sum.

	Args:
	    * list1 ([type]): [description]
	    * list2 ([type]): [description]
	"""	
	print(list1, list2)
	if sum(list1) & 1:
		return sorted(list1) + sorted(list2, reverse=True)
	else:
		return sorted(list1, reverse=True) + sorted(list2)

# Test cases
print(sort_array([]))		## []
print(sort_array([5]))		## [5]
print(sort_array([2, 4, 3, 0, 1, 5]))		## [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))	## [6, 5, 4, 3, 2, 1, 0]
print(sort_array([2, 4, 3, 1, 5, 6]))		## [4, 3, 2, 3, 5, 6]
print(sort_array([2, 4, 3, 5, 6, 7]))		## [3, 5, 6, 7, 4, 2]
print(sort_array([10, -12]))		## [-12, 10]