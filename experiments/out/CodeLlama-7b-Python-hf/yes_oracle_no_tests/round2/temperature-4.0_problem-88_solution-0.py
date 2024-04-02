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
    
	Do not include these tokens in the code: # Check to see if the array
	"""
    # check for the empty array
    if len(array) == 0:
        return array
    # check to see if the sum of the first and last index is odd
    if array[0] + array[-1] % 2 == 1:
        # if it is, sort it in ascending order
        array.sort()
    # if it is not, sort it in descending order
    else:
        array.sort(reverse=True)
    return array


def test_function(test_case):
    sorted_array = sort_array(test_case[0])
    print(sorted_array)
    if sorted_array == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_function([[], []])
test_function([[5], [5]])
test_function([[2, 4, 3, 0, 1, 5], [0, 1, 2, 3, 4, 5]])
test_function([[2, 4, 3, 0, 1, 5, 6], [6, 5, 4, 3, 2, 1, 0]])
test_function([[2, 4, 3, 0, 1, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1, 0]])
test_function([[2, 4, 3, 0, 1, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1, 0]])
