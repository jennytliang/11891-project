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

  # Add additional code here
  # return list
    if len(array) < 2:
        return array

    sum_of_first_last_elem = sum(array[0] + array[-1])
    if sum_of_first_last_elem % 2 == 0:
        array.sort(reverse=True)
    else:
        array.sort()

    return array


def test_function(test_case):
    array = test_case[0]
    solution = test_case[1]
    output = sort_array(array)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# test 1
array = []
solution = []
test_case = [array, solution]
test_function(test_case)

# test 2
array = [5]
solution = [5]
test_case = [array, solution]
test_function(test_case)

# test 3
array = [2, 4, 3, 0, 1, 5]
solution = [0, 1, 2, 3, 4, 5]
test_case = [array, solution]
test_function(test_case)

# test 4
array = [2, 4, 3, 0, 1, 5, 6]
solution = [6, 5, 4, 3, 2, 1, 0]
test_case = [array, solution]
test_function(test_case)
