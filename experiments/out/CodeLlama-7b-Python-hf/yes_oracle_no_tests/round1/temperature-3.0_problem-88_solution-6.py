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
    
	Include these tokens in the code: if array == [] : return
	Do not include these tokens in the code: sorted _ =
	"""
    result = []
    if array == []:
        return result
    if sum(array[0], array[-1]) % 2 == 0:
        for i in range(len(array)):
            result.append(array.pop(array.index(max(array))))
    else:
        for i in range(len(array)):
            result.append(array.pop(array.index(min(array))))
    return result


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
test_function([1, 2, 4, 3, 5, 0])
test_function([1, 2, 4, 3, 5, 0, 6])
test_function([0, 1, 2, 3, 4, 5])
test_function([0, 1, 2, 3, 4, 5, 6])
test_function([0, 1, 2, 3, 4, 5, 6, 7])
test_function([0, 1, 2, 3, 4, 5, 6, 7, 8])
test_function([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
test_function([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test_function([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
test_function([0,