def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # 1 . Br ute
	"""
    # TODO: Write your code here
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        return 0
    i = 0
    j = 1
    while j < n:
        if arr[j] > arr[i]:
            j += 1
        else:
            i += 1
            j += 1
    if arr[i] < arr[j]:
        return -1
    return i


test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_arrange(arr))
