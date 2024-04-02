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
    
	Do not include these tokens in the code: # find the sum of the
	"""
    if len(array) == 0: return []

    target_array = []

    for index, number in enumerate(array):
        target_array.append(array[len(array) - index - 1])
    
    sum_target = sum(target_array)

    if sum_target%2 == 0:
        # Sort target_array in ASC order
        target_array.sort()
    else:
        # Sort target_array in DESC order
        target_array.sort()
        target_array.reverse()

    return target_array

def test_function(test_case):
    array = test_case[0]
    solution = test_case[1]
    output = sort_array(array)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

#test_case A
array = [2, 4, 3, 0, 1, 5]
solution = [0, 1, 2, 3, 4, 5]

test_case = [array, solution]
test_function(test_case)

#test_case B
array = [2, 4, 4, 3, 3, 5, 7, 0, 9, 4, 5]
solution = [0, 1, 2, 3, 4, 5, 7, 9, 4, 4, 4]

test_case = [array, solution]
test_function(test_case)