def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def digits ( x : int ) -> int :
	"""
    from collections import deque
    q = deque()

    for i in range(k):
        if len(q) == 2:
            q.popleft()
        if len(q) == 0 or q[-1] < 10:
            q.append(arr[i])
        else:
            q.append(arr[i] % 10)

    return sum(q)


def add_elements_optimized(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def digits ( x : int ) -> int :
	"""
    i = 0
    total = 0
    while i < k:
        if len(str(arr[i])) > 2:
            arr[i] = arr[i] % 10
        total += arr[i]
        i += 1
    return total
