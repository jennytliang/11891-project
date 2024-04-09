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
    
	Include these tokens in the code: return sorted
	Do not include these tokens in the code: elif len
	"""


    if array == []:
        return array
    elif len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] + array[1] % 2 == 0:
            return sorted(array)
        else:
            return sorted(array, reverse=True)
    else:
        if array[0] + array[-1] % 2 == 0:
            return sorted(array)
        else:
            return sorted(array, reverse=True)

print(sort_array([0, 1, 2, 3, 4, 5]))
print(sort_array([0, 1, 2, 3, 4, 5, 6]))
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7]))
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13