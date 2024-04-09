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
    
	Include these tokens in the code: if array == [] : return []
	"""
    # array_copy = array.copy()
    # if len(array) == 0:
    #     return array
    # elif len(array) == 1:
    #     return array
    # elif len(array) == 2:
    #     if sum(array) % 2 == 0:
    #         return array[::-1]
    #     else:
    #         return array
    # else:
    #     if sum(array[:2]) % 2 == 0:
    #         array_copy.sort()
    #         return array_copy
    #     else:
    #         array_copy.sort(reverse=True)
    #         return array_copy

    # return array_copy

    # return array_copy

    # def get_sum(array):
    #     return sum(array[:2])

    # if len(array) == 0:
    #     return []
    # elif len(array) == 1:
    #     return array
    # elif len(array) == 2:
    #     if get_sum(array) % 2 == 0:
    #         return array[::-1]
    #     else:
    #         return array
    # else:
    #     if get_sum(array) % 2 == 0:
    #         array.sort()
    #         return array
    #     else:
    #         array.sort(reverse=True)
    #         return array

    # return array

    # def get_sum(array):
    #     return sum(array[:2])

    # if len(array) == 0:
    #     return []
    # elif len(array) == 1:
    #     return array
    # elif len(array) == 2:
    #     if get_sum(array) % 2 == 0:
    #         return array[::-1]
    #     else:
    #         return array
    # else:
    #     if get_sum(array) % 2 == 0:
    #        