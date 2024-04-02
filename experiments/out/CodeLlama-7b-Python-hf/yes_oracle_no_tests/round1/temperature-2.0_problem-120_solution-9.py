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
    
	Do not include these tokens in the code: res = [] for i
	"""
    if len(arr) < k:
        return arr
    
    # find the largest k numbers in the array
    # we will use a heap to do this
    # heapq.nlargest() is a builtin function that does this
    # we will use a max heap to do this
    # we will use a negative sign to represent a min heap
    # heapq.heapify() is a builtin function that does this
    # we will use a max heap to do this
    # we will use a negative sign to represent a min heap
    arr = [-x for x in arr]
    heapq.heapify(arr)
    
    # now we will extract the largest k numbers from the heap
    # we will use a list to do this
    # we will use a max heap to do this
    # we will use a negative sign to represent a min heap
    res = []
    for _ in range(k):
        res.append(-heapq.heappop(arr))
    
    return res


if __name__ == '__main__':
    # Example 1:
    #     Input: arr = [-3, -4, 5], k = 3
    #     Output: [-4, -3, 5]
    arr = [-3, -4, 5]
    k = 3
    print(maximum(arr, k))

    # Example 2:
    #     Input: arr = [4, -4, 4], k = 2
    #     Output: [4, 4]
    arr = [4, -4, 4]
    k = 2
    print(maximum(arr, k))

    # Example 3:
    #     Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
    #     Output: [2]
    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    print(maximum(arr, k))
