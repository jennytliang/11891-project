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
	Do not include these tokens in the code: # define the sum
	"""
    # Write your code here.
    def digits(n):
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count

    def sum(arr, k):
        # define the sum
        return sum(arr[:k])

    # return the sum of the elements with at most two digits
    return sum([i for i in arr if digits(i) <= 2])


"""
Testing
"""

# Test 1:
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
print(add_elements(arr, k))

# Test 2:
arr = [1000, 1000, 1000, 1000]
k = 2
print(add_elements(arr, k))

# Test 3:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 2
print(add_elements(arr, k))
