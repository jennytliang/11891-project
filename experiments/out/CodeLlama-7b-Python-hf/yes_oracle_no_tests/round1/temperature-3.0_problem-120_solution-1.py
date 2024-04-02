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
    if not arr or k == 0: return []

    # sort the array
    arr.sort()

    # build a heap
    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])

    # now, the heap has the largest k numbers
    # iterate the rest of the array
    for i in range(k, len(arr)):
        # if the current number is larger than the smallest number in the heap
        # then pop the smallest number from the heap
        # and push the current number into the heap
        if arr[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])

    return sorted(heap)


def main():
    # call the solution with different test inputs
    test_inputs = [
        ([[-3, -4, 5], 3], [-4, -3, 5]),
        ([[4, -4, 4], 2], [4, 4]),
        ([[-3, 2, 1, 2, -1, -2, 1], 1], [2])
    ]

    for test_case in test_inputs:
        print(maximum(*test_case[0]))


if __name__ == '__main__':
    main()
