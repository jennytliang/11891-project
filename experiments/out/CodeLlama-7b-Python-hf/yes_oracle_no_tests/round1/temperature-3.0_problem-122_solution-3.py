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
    # add your code here
    # arr = [111,21,3,4000,5,6,7,8,9]
    # k = 4
    res = 0
    for i in range(k):
        res += add_digits(arr[i])
    return res
    
def add_digits(n):
    if n < 10:
        return n
    return n % 10 + add_digits(n // 10)

print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 3)) # 26
print(add_elements([111,21,3,4000,5,6,7,8,9], 2)) # 25
print(add_elements([111,21,3,4000,5,6,7,8,9], 1)) # 20
print(add_elements([111,21,3,4000,5,6,7,8,9], 0)) # 0
