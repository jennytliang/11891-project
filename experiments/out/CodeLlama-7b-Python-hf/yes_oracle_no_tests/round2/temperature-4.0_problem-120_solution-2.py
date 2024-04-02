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
    
	Include these tokens in the code: return sorted ( sorted
	Do not include these tokens in the code: if not arr or k > len
	"""
    from collections import defaultdict
    # from sortedcontainers import SortedList

    # Solution 1:
    # def maximum(arr, k):
    #     """
    #     Sort the whole array, and return the first k numbers.
    #     """
    #     arr.sort(reverse=True)
    #     return arr[:k]
    #
    # Solution 2:
    # def maximum(arr, k):
    #     """
    #     Use a heap to store the k largest numbers.
    #     """
    #     from heapq import heappush, heappop
    #     heap = []
    #     for num in arr:
    #         heappush(heap, num)
    #         if len(heap) > k:
    #             heappop(heap)
    #     return sorted(heap, reverse=True)

    # Solution 3:
    # def maximum(arr, k):
    #     """
    #     Use a heap to store the k largest numbers.
    #     """
    #     from heapq import heappush, heappop
    #     heap = []
    #     for num in arr:
    #         heappush(heap, num)
    #         if len(heap) > k:
    #             heappop(heap)
    #     return heap

    # Solution 4:
    # def maximum(arr, k):
    #     """
    #     Use a heap to store the k smallest numbers.
    #     """
    #     from heapq import heappush, heappop
    #     heap = []
    #     for num in arr:
    #         heappush(heap, -num)
    #         if len(heap) > k:
    #             heappop(heap)
    #     return [-x for x in heap]

    # Solution 5:
    # def maximum(arr, k):
    #     """
    #     Use a heap to store the k smallest numbers.
    #     """
    #     from heapq import heapp