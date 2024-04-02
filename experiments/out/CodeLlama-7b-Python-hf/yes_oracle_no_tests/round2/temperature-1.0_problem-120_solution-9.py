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
    
	Include these tokens in the code: return sorted
	Do not include these tokens in the code: # Time Complex ity : O
	"""
    n = len(arr)
    k = k if k <= n else n
    heap = list()
    for i in range(k):
        heap.append(arr[i])
        
    
    for i in range(k, n):
        # if heap[-1] < arr[i]:
            # heapq.heapreplace(heap, arr[i])
        # else:
            # heapq.heappush(heap, arr[i])
        # heap[0] = arr[i] will update the minimum as well
        # heap = sorted(heap)
        heap[0] = arr[i]
        heap.sort()
    heap.sort()
    return heap


if __name__ == "__main__":
    test_cases = [
        [-3, -4, 5],
        [4, -4, 4],
        [-3, 2, 1, 2, -1, -2, 1],
        [4, 4, 4],
        [-20, 100, 200, 90, 70, 101, 71, 0],
    ]
    k_list = [3, 2, 1, 1, 4]
    expected_answers = [
        [-4, -3, 5],
        [4, 4],
        [2],
        [4, 4],
        [71, 0, 200, 101, 100]
    ]

    for test_case, k, expected_answer in zip(test_cases, k_list, expected_answers):
        assert maximum(test_case, k) == expected_answer


#    def minimum_subset_sum_difference(self, arr):
#        """
#        Given an array arr of integers, return the difference between 
#        the sum of its maximum subarray and minimum subarray.
#
#        Example 1:
#        Input: arr = [75, 15, 21, 55]
#       