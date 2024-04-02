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
    count = 0
    result = 0
    for i in range(k):
        result += count_digits(arr[i])
        count += 1
        if count == 2:
            result -= count_digits(arr[i])
            count = 0
    return result

def count_digits(x):
    count = 0
    while x > 0:
        x = x // 10
        count += 1
    return count

print(count_digits(5))
print(count_digits(123))
print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
print(add_elements([1, 2, 3, 4, 5], 2))
print(add_elements([1, 2, 3, 4, 5], 5))
print(add_elements([1, 2, 3, 4, 5], 4))
print(add_elements([111,21,3,4000,5,6,7,8,9], 1))
print(add_elements([111,21,3,4000,5,6,7,8,9], 10))
print(add_elements([111,21,3,4000,5,6,7,8,9], 8))
print(add_elements([111,21,3,4000,5,6,7,8,9], 9))
print(add_elements([111,21,3,4000,5,6,7,8,9], 100))
print(add_elements([1111111111111111,21,3,4000,5,6,7,8,9], 100))