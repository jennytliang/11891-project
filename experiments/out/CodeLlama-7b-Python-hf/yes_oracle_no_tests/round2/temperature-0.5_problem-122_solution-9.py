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
    
	Do not include these tokens in the code: # O ( n ) time
	"""
    # O(n log n) time
    arr.sort()
    return sum(arr[:k])


def add_elements_v2(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
    Do not include these tokens in the code: # O ( n ) time
    """
    # O(n) time
    count = 0
    for i in range(k):
        count += arr[i]
    result = count

    for i in range(k, len(arr)):
        count = count - arr[i - k] + arr[i]
        result = max(result, count)
    return result


print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
print(add_elements_v2([111,21,3,4000,5,6,7,8,9], 4))