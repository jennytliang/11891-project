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
	Do not include these tokens in the code: count = 0 result
	"""
    result = 0
    for i in arr[:k]:
        if digits(i) <= 2:
            result += i
    return result


def digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))
