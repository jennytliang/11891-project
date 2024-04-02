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
    
	Include these tokens in the code: def digits
	Do not include these tokens in the code: s = 0 for
	"""
    # s = 0
    # for i in range(k):
    #     s += digits(arr[i])
    # return s

    return digits(arr[0]) + digits(arr[k-1])

def digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
