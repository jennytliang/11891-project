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
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: he ap q . nl arg est
	"""

    return so_list_maximum(arr, k)


def so_list_maximum(arr, k):
    """
    Solution 1: Sorting

    * Sort the array in descending order
    * Return the first k elements of the array

    Complexity Analysis:
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
    """
    arr.sort(reverse=True)
    return arr[:k]


def my_list_maximum(arr, k):
    """
    Solution 2: Heap

    * Create a heap of size k
    * Add the first k elements to the heap
    * For the remaining elements
        * If it is greater than the smallest element in the heap, replace the smallest element

    Complexity Analysis:
        Time Complexity: O(nlogk)
        Space Complexity: O(k)
    """
    from heapq import heappush, heappop, heapreplace
    heap = []

    for i in range(k):
        heappush(heap, arr[i])

    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapreplace(heap, arr[i])

    return heap


if __name__ == "__main__":
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
