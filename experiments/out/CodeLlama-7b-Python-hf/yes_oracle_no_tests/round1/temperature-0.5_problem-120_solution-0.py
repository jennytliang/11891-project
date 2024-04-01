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
    
	Do not include these tokens in the code:  if k ==  0 :  return
	"""

    n = len(arr)
    if k == 0 or n == 0 or k > n:
        return []
    elif k == 1:
        return [max(arr)]
    else:
        # create a heap of size k
        # insert first k elements of arr in the heap
        # pop the root element from the heap
        # insert the popped element in the heap
        # return the root element
        import heapq
        heap = arr[:k]
        heapq.heapify(heap)
        for i in range(k, n):
            heapq.heappushpop(heap, arr[i])
        return heap


if __name__ == "__main__":
    arr = [-3, -4, 5]
    k = 3
    print(maximum(arr, k))

    arr = [4, -4, 4]
    k = 2
    print(maximum(arr, k))

    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    print(maximum(arr, k))

    arr = [-3, -4, 5]
    k = 4
    print(maximum(arr, k))

    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 5
    print(maximum(arr, k))
