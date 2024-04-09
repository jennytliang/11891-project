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
    
	Do not include these tokens in the code: from collections import default dict
	"""
    if k >= len(arr):
        return sorted(arr)
    if k == 0:
        return []
    if k == 1:
        return [max(arr)]

    # use heapq.nlargest to get the top k numbers
    # return nlargest(k, arr)

    # use heapq.heapify and heapq.heappop to get the top k numbers
    # heapq.heapify(arr)
    # res = []
    # for i in range(k):
    #     res.append(heapq.heappop(arr))
    # return res

    # use heapq.heappushpop to push and pop
    # heap = []
    # for num in arr:
    #     if len(heap) < k:
    #         heapq.heappush(heap, num)
    #     else:
    #         heapq.heappushpop(heap, num)
    # return heap
    
    # use heapq.heappush to push and pop
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
    return heap


if __name__ == "__main__":
    arr = [4, -4, 4]
    k = 2
    print(maximum(arr, k))
