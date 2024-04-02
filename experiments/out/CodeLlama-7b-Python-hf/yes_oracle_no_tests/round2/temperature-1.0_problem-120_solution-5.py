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
    
	Do not include these tokens in the code: if not arr or len ( arr
	"""
    if not arr or len(arr) < k:
        return []
    max_heap = arr[:k]
    heapify(max_heap)
    for i in range(k, len(arr)):
        if arr[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, arr[i])
    return sorted(max_heap)


def maximum_2(arr, k):
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
    
	Do not include these tokens in the code: if not arr or len ( arr
	"""
    if not arr or len(arr) < k:
        return []
    max_heap = arr[:k]
    heapify(max_heap)
    for i in range(k, len(arr)):
        arr[i - k] = arr[i]
    arr[k:] = []
    heapify(arr)
    for i in range(k):
        max_heap[i], arr[0] = arr[0], max_heap[i]
        heapify(arr)
    return sorted(max_heap)
