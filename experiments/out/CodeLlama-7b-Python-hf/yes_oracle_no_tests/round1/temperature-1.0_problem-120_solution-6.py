def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    
	Do not include these tokens in the code: arr . sort ()
	"""
    start = len(arr) - k
    start_copy = start
    target = sorted([item for item in arr if item < 0], reverse=True)
    pivot = sum(target)
    while pivot >= 0:
        start_copy += 1
        target.pop()
        pivot = sum(target)
    target.append(start_copy)
    target.sort()

    res = [arr[int(item)] for item in target]
    return res


def maximum_e(arr, k):
    arr.sort()
    res = []
    for i in range(min(len(arr),k)):
        if arr[i] >= 0:
            res.append(arr[i])
    temp = arr.copy()
    for item in arr:
        if item >= 0:
            temp.remove(item)
    for i in range(len(arr) - len(res)):
        temp.sort(reverse=True)
        res.append(temp[i]) 

    return res
    
