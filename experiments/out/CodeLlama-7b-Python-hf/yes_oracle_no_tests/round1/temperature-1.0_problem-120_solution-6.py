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
    if not arr or k == 0: return []
    if k >= len(arr): return sorted(arr)

    # find the largest k numbers
    max_heap = [(-arr[0], 0)] # store (priority, idx)
    for i in range(1, k):
        while max_heap and arr[max_heap[-1][1]] < -max_heap[-1][0]:
            heapq.heappop(max_heap)
        heapq.heappush(max_heap, (-arr[i], i))

    # find the smallest k numbers
    min_heap = [arr[0]]
    for i in range(1, k):
        while min_heap and arr[min_heap[-1]] < min_heap[-1]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, arr[i])

    # find the median of the largest k numbers and the smallest k numbers
    return sorted(min_heap + [arr[i] for _, i in max_heap] + min_heap)


def main():
    # call the method with the following parameters
    #   arr = [-3, -4, 5]
    #   k = 3
    result = maximum(arr, k)
    print(result)  # [-4, -3, 5]

    # call the method with the following parameters
    #   arr = [4, -4, 4]
    #   k = 2
    result = maximum(arr, k)
    print(result)  # [4, 4]

    # call the method with the following parameters
    #   arr = [-3, 2, 1, 2, -1, -2, 1]
    #   k = 1
    result = maximum(arr, k)
    print(result)  # [2]


if __name__ == '__main__':
    main()
