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


    if not array:
        return []

    # check if the sum( first index value, last index value) is odd or even
    if sum(array) % 2 == 0:
        sorted_array = sorted(array, reverse=True)
    else:
        sorted_array = sorted(array)

    return sorted_array



def test_function(test_case):
    array = test_case[0]
    solution = test_case[1]
    output = sort_array(array)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


# test case 1 - empty array
test_case_1 = ([], [])

# test case 2 - array with one element
test_case_2 = ([5], [5])

# test case 3 - array with two elements
test_case_3 = ([2, 4], [2, 4])

# test case 4 - array with three or more elements
test_case_4 = ([2, 4, 3, 0, 1, 5], [0, 1, 2, 3, 4, 5])

# test case 5 - array with three or more elements
test_case_5 = ([2, 4, 3, 0, 1, 5, 6], [6, 5, 4, 3, 2, 1, 0])

# test case 6 - array with odd sum
test_case_6 = ([2, 4, 3, 0, 1, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7])

# test case 7 - array with even sum
test_case_7 = ([2, 4, 3, 0, 1, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1, 0])

test_function(test_case_1)
test_function