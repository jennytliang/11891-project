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
    if len(array) <= 1:
        return array
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
test_function([2, 2, 2, 2, 2, 2])
test_function([1, 2, 3, 4])
test_function([2, 1, 3, 4])
test_function([3, 2, 1, 4])
test_function([4, 3, 2, 1])
test_function([1, 3, 2, 4])
test_function([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
