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
    
	Do not include these tokens in the code: # Write your code here .
	"""
    # Write your code here.
    return sum(arr[:k])

if __name__ == '__main__':
    # Test 1
    arr = [111,21,3,4000,5,6,7,8,9]
    k = 4
    print(add_elements(arr, k))

    # Test 2
    arr = [1,2,3,4,5,6,7,8,9]
    k = 4
    print(add_elements(arr, k))

    # Test 3
    arr = [111,21,3,4000,5,6,7,8,9]
    k = 4
    print(add_elements(arr, k))
