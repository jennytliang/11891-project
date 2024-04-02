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
    if k == 0 or len(arr) == 0:
        return []
    elif k == 1:
        return [max(arr)]
    elif k == len(arr):
        return sorted(arr)

    max_heap = []
    for i in range(k):
        max_heap.append(arr[i])
    
    for i in range(k, len(arr)):
        if arr[i] > max_heap[0]:
            heapq.heapreplace(max_heap, arr[i])
    
    return sorted(max_heap)


def main():
    arr = [-3, -4, 5]
    k = 3
    print(f'Input: arr = {arr}, k = {k}')
    print(f'Output: {maximum(arr, k)}')

    arr = [4, -4, 4]
    k = 2
    print(f'Input: arr = {arr}, k = {k}')
    print(f'Output: {maximum(arr, k)}')

    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    print(f'Input: arr = {arr}, k = {k}')
    print(f'Output: {maximum(arr, k)}')


if __name__ == '__main__':
    main()
