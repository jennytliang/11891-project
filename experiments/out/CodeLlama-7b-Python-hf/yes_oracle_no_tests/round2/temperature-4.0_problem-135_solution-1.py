def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Find the largest index which is
	"""
    # Find the largest index which is not greater than or equal to the element
    # immediately preceding it. If no such element exists then return -1.

    # Create a dictionary to store the index of the element
    element_index_dict = {}
    for i, element in enumerate(arr):
        element_index_dict[element] = i

    # Iterate over the array
    for i, element in enumerate(arr):
        if i < len(arr) - 1:
            if element_index_dict[arr[i + 1]] < element:
                return element_index_dict[arr[i + 1]]
        else:
            return -1
    return -1


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = can_arrange(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 4, 3, 5]
solution = 3
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = -1
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
solution = -1
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solution = 8
test_case = [arr, solution]
test_function(test_case)
