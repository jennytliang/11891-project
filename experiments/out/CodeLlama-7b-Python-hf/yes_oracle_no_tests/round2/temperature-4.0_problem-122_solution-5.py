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
	Do not include these tokens in the code: from collections import de que
	"""
    # init
    answer = 0
    k = min(k, len(arr))

    # for each element in arr, check if it has 2 or less digits
    for i in range(k):
        if digits(arr[i]) <= 2:
            answer += arr[i]

    return answer


def digits(n):
    """
    Count the number of digits in a number

    Example:
        Input: 12345
        Output: 5

    Constraints:
        1. 0 <= n <= 2^64 - 1
    """
    # init
    count = 0

    # check if n is positive or negative
    if n < 0:
        n *= -1

    # while n is greater than 0
    while n > 0:
        n = n // 10
        count += 1

    return count


print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 6))
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 9))
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 10))
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 11))
