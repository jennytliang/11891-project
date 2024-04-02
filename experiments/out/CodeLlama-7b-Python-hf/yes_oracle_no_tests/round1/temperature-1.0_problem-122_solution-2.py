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
    # Sum of the first k elements
    sum = 0
    count = 0
    while k > 0:
        if count == len(arr):
            return sum
        x = arr[count]
        len_first_k = False
        for digit in str(x):
            if len(digit) >= k:
                len_first_k = True
                break
        if not len_first_k:
            sum += x
            k -= 1
        count += 1

    return sum

# print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
# print(add_elements([11,21,3,4000,5,6,7,8,9], 4))