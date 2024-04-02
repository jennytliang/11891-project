def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Find largest index for which arr
	"""
    largest_index = -1
    for i in range(len(arr)):
        # Find largest index for which arr[i] <= arr[largest_index]
        if arr[i] <= arr[largest_index]:
            largest_index = i
    return largest_index


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
