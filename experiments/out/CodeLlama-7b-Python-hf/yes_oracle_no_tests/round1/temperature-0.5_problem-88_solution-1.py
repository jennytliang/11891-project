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

    if lenth(array) == 0:
        return []

    if lenth(array) == 1:
        return array

    if lenth(array) == 2:
        if sum(array[0], array[1]) % 2 == 0:
            return array
        else:
            return [array[1], array[0]]

    if lenth(array) == 3:
        if sum(array[0], array[1], array[2]) % 2 == 0:
            return array
        else:
            return [array[2], array[1], array[0]]

    if lenth(array) == 4:
        if sum(array[0], array[1], array[2], array[3]) % 2 == 0:
            return array
        else:
            return [array[3], array[2], array[1], array[0]]

    if lenth(array) == 5:
        if sum(array[0], array[1], array[2], array[3], array[4]) % 2 == 0:
            return array
        else:
            return [array[4], array[3], array[2], array[1], array[0]]

    if lenth(array) == 6:
        if sum(array[0], array[1], array[2], array[3], array[4], array[5]) % 2 == 0:
            return array
        else:
            return [array[5], array[4], array[3], array[2], array[1], array[0]]

    if lenth(array) == 7:
        if sum(array[0], array[1], array[2], array[3], array[4], array[5], array[6]) % 2 == 0:
            return array
        else:
            return [array[6], array[5], array[4], array[3], array[2], array[1], array[0]]

    if lenth(array) == 8:
        if sum(array[0], array[1], array[2], array[3