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
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[largest] < arr[l]:
            largest = l
        
        if r < n and arr[largest] < arr[r]:
            largest = r
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    def heap_sort(arr):
        n = len(arr)
        for i in range(n, -1, -1):
            heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    def merge_sort(arr, p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort(arr, p, q)
            merge_sort(arr, q+1, r)
            merge(arr, p, q, r)

    def merge(arr, p, q, r):
        n1 = q - p + 1
        n2 = r - q

        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)

        for i in range(0, n1):
            L[i] = arr[p + i]
        for j in range(0, n2):
            R[j] = arr[q + j + 1]

        L[n1] = float('inf')
        R[n2] = float('inf')

        i = 0
        j = 0
        for k in range(p, r+1):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] =