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
    
	Include these tokens in the code: if array == [] : return [] return
	"""
    # return array not sorted if sum(array).is_odd()
    if sum(array) & 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)


"""
    FUNCTION NAME: sort_array 
    TYPE:
    PURPOSE:
    PARAMETERS:
    RETURN VALUE:
    EXAMPLES:
"""


def test_case(array, result):
    output = sort_array(array)
    if output == result:
        print("Passed")
    else:
        print("Failed")


def test():
    # Do not change this array
    array = [1, 3, 2, 0, 8, 99]
    result = [0, 1, 2, 3, 8, 99]
    test_case(array, result)

    array = [3, 0, 99, 6, 2]
    result = [2, 6, 3, 0, 99]
    test_case(array, result)

    array = [0, 0, 0, 0, 0]
    result = [0, 0, 0, 0, 0]
    test_case(array, result)

    array = [1, 2, 3, 0, 5, 6]
    result = [0, 1, 2, 3, 5, 6]
    test_case(array, result)


test()
