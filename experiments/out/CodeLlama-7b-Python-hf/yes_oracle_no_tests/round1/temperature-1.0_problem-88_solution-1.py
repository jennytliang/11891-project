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
	array_length = len(array)
	if(array_length == 0 ):
		return []
	else:
		if((sum(array[0], array[-1])) % 2 == 0):
			array = array[(array_length//2):(array_length)] + array[:(array_length//2)]
		else:
			array = array[(array_length//2):(array_length)] + array[:(array_length//2)][::-1]
			#print( array[(array_length//2):(array_length)] , array[:(array_length//2)][::-1] )
	return array

"""Answer:
array = []
array_length = len(array)

if(array_length == 0 )
    return array
else:
    sorted_array = []
	if((sum_of_array(array[0], array[-1])) % 2 == 0):
		for item in reversed(array):
			sorted_array.append(item)
	else:
        for item in array:
            sorted_array.append(item)
	return sorted_array
"""
'''
if(array_length > 0):
	if((sum_of_array(array[0], array[-1])) % 2 == 0):
		for item in sorted(array[::-1]):
			sorted_array.append(item)
	else:
		for item in sorted(array):
			sorted_array.apend(item)
	return sorted_array
'''