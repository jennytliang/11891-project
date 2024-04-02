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
	Do not include these tokens in the code: if len
	"""
    n = 0
    m = 0
    total = 0
    for i in range(min(len(arr), k) + 1):
        if len(str(arr[i])) > 2 or n == 2:
            total += m
            n = 0
            m = 0
        n += 1
        m += arr[i]
        
    total += m
    return total



print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
print(add_elements([253,299,333,400,5,6,7,8,9], 2))
print(add_elements([111,21,3,4000,5,6,7,8,9], 2))
print(add_elements([ 866777888, 866532781, 86712389, 898876555, 8988899], 5))


"""
Time complexity: O(n+k)

Space complexity: O(1) 
"""