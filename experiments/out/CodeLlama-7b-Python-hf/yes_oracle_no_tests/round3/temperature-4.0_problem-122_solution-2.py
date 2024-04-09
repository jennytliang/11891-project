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
    
	Include these tokens in the code: def digits ( x : int ) -> int
	Do not include these tokens in the code: # Add your code here
	"""
    return sum(str(e)[:2] for e in arr[:k])

print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
print(add_elements([1,2,3,4,5,6,7,8,9], 4))
print(add_elements([1111,21,3,4000,5,6,7,8,9], 4))
print(add_elements([111,21,3,4000,5,6,7,8,9], 3))
print(add_elements([111,21,3,4000,5,6,7,8,9], 2))
print(add_elements([111,21,3,4000,5,6,7,8,9], 1))
print(add_elements([111,21,3,4000,5,6,7,8,9], 0))
print(add_elements([1], 0))
print(add_elements([1,2,3,4,5,6,7,8,9], 100))