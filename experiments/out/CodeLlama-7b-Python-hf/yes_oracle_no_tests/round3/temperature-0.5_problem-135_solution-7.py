def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: ) - 1 , 0 , - 1
	Do not include these tokens in the code: )):
	"""

    for i in range(le(arr)):
        if arr[i] > arr[le(arr[i:])]:
            return i
    return -1


def le(arr):
    return len(arr) - 1


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = can_arrange(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# Tests
test_function([[1, 2, 4, 3, 5], 3])
test_function([[1, 2, 3], -1])
test_function([[1, 3, 5, 2, 4], 4])
test_function([[2, 4, 3, 5, 1], 4])
