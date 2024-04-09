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
    
	Include these tokens in the code: )[ :: - 1 ][ :
	Do not include these tokens in the code: ) [:
	"""


    return sorted(sort_k_elements(arr, k), reverse=True)


def sort_k_elements(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr[:k]

    # find the minimum of k elements in arr
    # since we need to find the maximum k elements in arr, we use the minimum
    # to find the maximum
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    # find the k elements
    k_elements = [arr[min_idx]]
    arr[min_idx] = float('inf')
    for i in range(k - 1):
        min_idx = 0
        for j in range(1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        k_elements.append(arr[min_idx])
        arr[min_idx] = float('inf')

    return k_elements


def test_maximum():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 2) == [2, 2]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 3) == [-3, 2, 2]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 4) == [-3,