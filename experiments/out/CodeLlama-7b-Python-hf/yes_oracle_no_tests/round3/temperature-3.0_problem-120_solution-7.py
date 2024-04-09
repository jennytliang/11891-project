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
    
	Include these tokens in the code: sorted (
	"""

    return so_max_heap(arr, k)


def so_max_heap(arr, k):
    # create a heap of size k
    heap = Heap(max)

    for i in range(k):
        heap.insert(arr[i])

    for i in range(k, len(arr)):
        if arr[i] > heap.peek():
            heap.extract()
            heap.insert(arr[i])

    return heap.to_list()


class Heap:
    def __init__(self, comparator):
        self.heap = []
        self.comparator = comparator

    def __len__(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)

        return root

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def to_list(self):
        return self.heap

    def _sift_up(self, idx):
        if idx == 0:
            return

        parent = (idx - 1) // 2
        if self.comparator(self.heap[parent], self.heap[idx]) > 0:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            self._sift_up(parent)

    def _sift_down(self, idx):
        left = (idx + 1) * 2 - 1
        right = (idx + 1) * 2

        largest =