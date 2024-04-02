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
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # for loop through
	"""
    if len(array) == 0:
        return []

    if len(array) == 1:
        return array

    if len(array) == 2:
        return [min(array), max(array)]

    if len(array) > 2:
        if sum(array[0]) + sum(array[-1]) % 2 == 0:
            return sorted(array)
        else:
            return sorted(array, reverse=True)


def test_function(test_case):
    sorted_array = sort_array(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([])
test_function([5])
test_function([2, 4, 3, 0, 1, 5])
test_function([2, 4, 3, 0, 1, 5, 6])
test_function([2, 4, 3, 5, 6, 0, 1])
test_function([2, 4, 3, 5, 6, 0, 1, 7])
test_function([2, 4, 3, 5, 6, 0, 1, 7, 8])
