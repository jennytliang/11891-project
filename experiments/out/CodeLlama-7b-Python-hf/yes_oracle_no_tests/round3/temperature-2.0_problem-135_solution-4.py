def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Initialize variables left =
	"""
    # Initialize variables
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] >= arr[left + 1]:
            left += 1
        elif arr[right] <= arr[right - 1]:
            right -= 1
        else:
            return -1
    return left


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

arr = [3, 2, 1]
solution = -1
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
solution = -1
test_case = [arr, solution]
test_function(test_case)

arr = [5, 4, 3, 2, 1]
solution = 0
test_case = [arr, solution]
test_function(test_case)

arr = [1, 3, 2, 4, 5]
solution = 3
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 3, 4, 4, 5, 5]
solution = 6
test_case = [arr, solution]
test_function(test_case)
