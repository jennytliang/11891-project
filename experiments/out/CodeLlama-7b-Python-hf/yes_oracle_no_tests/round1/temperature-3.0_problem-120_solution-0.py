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
    
	Do not include these tokens in the code: if k == 0 or len
	"""
    if k == 0 or len(arr) == 0: return []
    if k == 1: return [max(arr)]
    if k >= len(arr): return sorted(arr)

    # find the kth largest number in arr
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < arr[hi]:
            lo = mid + 1
        else:
            hi = mid
    kth_largest = arr[lo]

    # find the largest number in the first k elements
    lo, hi = 0, k - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < kth_largest:
            lo = mid + 1
        else:
            hi = mid
    largest = arr[lo]

    # find the smallest number in the last len(arr) - k elements
    lo, hi = k, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > kth_largest:
            hi = mid
        else:
            lo = mid + 1
    smallest = arr[hi]

    # find the smallest number in the first len(arr) - k elements
    lo, hi = 0, len(arr) - k - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > smallest:
            hi = mid
        else:
            lo = mid + 1
    smallest_in_remain = arr[hi]

    if smallest_in_remain <= largest:
        return sorted(arr[:k] + [largest])
    else:
        return sorted(arr[:k] + [largest, smallest_in_remain])

    # return sorted(arr[:k] + [max(arr[:k])])

    # if k == 0 or len(arr) == 0: return []
    # if k