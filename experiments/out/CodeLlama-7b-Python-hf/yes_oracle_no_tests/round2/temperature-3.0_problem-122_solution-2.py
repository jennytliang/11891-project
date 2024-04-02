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
	Do not include these tokens in the code: ### ######## ## # Base
	"""
    arr = arr[:k]
    return sum([number for number in arr if len(str(number)) <= 2])


print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 10))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 5))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 1))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 2))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 3))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 4))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 5))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 6))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 7))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 8))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 9))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 10))
print(add_elements([0,1,2,3,4,5,6,7,8,9,10], 11))


def