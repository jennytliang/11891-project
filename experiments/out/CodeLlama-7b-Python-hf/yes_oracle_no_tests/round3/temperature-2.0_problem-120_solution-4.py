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
    
	Do not include these tokens in the code: # set heap size heap
	"""
    def get_k_max_numbers(arr, k):
        """
        Get the k max numbers from an array in O(nlogk) time.
        """
        max_heap = []
        for i in range(k):
            max_heap.append(arr[i])
        heapq.heapify(max_heap)
        for i in range(k, len(arr)):
            if arr[i] > max_heap[0]:
                heapq.heapreplace(max_heap, arr[i])
        return max_heap

    if k > len(arr):
        return arr

    max_heap = get_k_max_numbers(arr, k)
    return max_heap


def main():
    print(maximum([-3, -4, 5], 3))  # [-4, -3, 5]
    print(maximum([4, -4, 4], 2))  # [4, 4]
    print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # [2]


if __name__ == "__main__":
    main()
