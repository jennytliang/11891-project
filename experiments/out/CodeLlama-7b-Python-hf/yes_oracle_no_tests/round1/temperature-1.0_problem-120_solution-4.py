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
    # convert to max heap
    for i in range((len(arr))//2-1, -1, -1):
        parent_index = i
        swap = i
        for j in range(parent_index*2 + 1, i*2 + 1):
            if j + 1 <= len(arr) - 1\
            and ((arr[j] > arr[j+1] and arr[parent_index] < arr[j+1]) or\
             arr[parent_index] < arr[j]):
                swap = j + 1
        if swap != parent_index:
            arr[parent_index], arr[swap] = arr[swap], arr[parent_index]
    
    max_arr = []  # max heap for max k numbers
    max_count = 0
    
    # compare with k numbers and swap the bigger one
    for i in range(k):
        if max_count < k and arr[-1] > max_arr[max_count - 1]:
            max_arr[-max_count - 1], max_arr[max_count] = max_arr[max_count], max_arr[-max_count - 1]
            max_count += 1
            continue

        max_arr.pop()
        for j in range((len(arr))//2 - 1, -1, -1):
            parent_index = j
            swap = j
            for k in range(parent_index*2 + 1, j*2 + 1):
                if k + 1 <= len(arr) - 1\
                and ((arr[k] > arr[k+1] and arr[parent_index] < arr[k+1]) or\
                 arr[parent_index] < arr[k]):
                    swap = k + 1
            if swap != parent_index:
                arr[parent_index], arr[swap] = arr[swap], arr[parent_index]
                max_arr.append(arr[-1])
    return max_arr


arr = [-4, -2, 2, 1, -1, 0, -