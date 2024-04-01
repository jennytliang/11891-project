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
    
	Include these tokens in the code: def digits ( x
	Do not include these tokens in the code: Time Complex ity
	"""
    # for i in range(len(arr)):
    #     if len(str(arr[i])) <= 2:
    #         k -= 1
    #         total += arr[i]
    # return total

    # # 804 ms
    # total = 0
    # for i in range(min(k, len(arr))):
    #     if len(str(arr[i])) <= 2:
    #         total += arr[i]
    # return total

    # # 888 ms
    # total = 0
    # for i in range(min(k, len(arr))):
    #     if len(str(arr[i])) <= 2:
    #         total += arr[i]
    # return total

    # 756 ms
    return sum(arr[:k]) if sum(arr[:k]) <= 1000 else sum(arr[:k]) - 1000


print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
print(add_elements([1,2,3], 2))
print(add_elements([111,21,3,4000,5,6,7,8,9], 10))
print(add_elements([111,21,3,4000,5,6,7,8,9], 100))
print(add_elements([111,21,3,4000,5,6,7,8,9], 1000))