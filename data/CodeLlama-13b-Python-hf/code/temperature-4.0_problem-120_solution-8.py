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
    """
    heap = [[a, idx] for idx, a in enumerate(arr)]
    kk = len(arr)
    h = []
    print(h)
    
    heapq.heapsort(heap) 

    for i in range(kk):
        print(h, i, k)   
        if i<=k:
            print('kk', kk) 
            if i == k : return [heap[a for _, a in h]]
            if i == 0: h.append( heap.pop(i) )
        else: 
            print( i==k, heap, h)  
    
            # print(h )
    if i == k: 
        # print(h)          
        print('last h', i, h)
        m = []
        # if k:
        print('i==k', h, heap)
        