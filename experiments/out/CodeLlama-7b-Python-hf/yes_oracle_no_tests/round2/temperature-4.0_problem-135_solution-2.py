def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len ( arr ) -
	"""
    # arr = [1, 2, 4, 3, 5]
    # arr = [1, 2, 3]
    # if len(arr) == 1:
    #     return -1
    # if arr[-1] < arr[-2]:
    #     return len(arr) - 1
    # for i in range(len(arr) - 2, -1, -1):
    #     if arr[i] < arr[i+1]:
    #         return i
    # return -1

    # # One liner
    # return max(i for i in range(len(arr) - 1) if arr[i] < arr[i + 1])

    # # One liner
    # return next((i for i in range(len(arr) - 1) if arr[i] < arr[i + 1]), -1)

    # # One liner
    # return next((i for i in range(len(arr) - 1) if arr[i] < arr[i + 1]), -1)

    # # One liner
    # return next((i for i in range(len(arr) - 1) if arr[i] < arr[i + 1]), -1)

    # One liner
    return next((i for i in range(len(arr) - 1) if arr[i] < arr[i + 1]), -1)


print(can_arrange([1, 2, 4, 3, 5]))  # 3
print(can_arrange([1, 2, 3]))  # -1
print(can_arrange([1, 2, 3, 4]))  # -1
print(can_arrange([1, 2, 3, 4, 5]))  # -1
print(can_arrange([1, 2, 3, 4, 5, 6]))  # -1
print(can_arrange([1, 2, 3, 4, 5, 6, 7]))  # -1