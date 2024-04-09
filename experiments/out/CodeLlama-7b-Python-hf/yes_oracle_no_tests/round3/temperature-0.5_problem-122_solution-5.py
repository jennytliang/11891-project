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

    # 1. Brute-force O(n^2)
    #   - sum up the elements with at most two digits from the first k elements of arr
    #   - use a counter for the number of elements with at most two digits
    #     - for each element in the first k elements, check if it has at most two digits
    #     - if it does, add it to the sum and increment the counter
    #   - return the sum
    #
    #   Time: O(k)
    #   Space: O(1)
    #
    # def add_elements(arr, k):
    #     # 1. initialize our sum to 0
    #     sum = 0
    #
    #     # 2. loop through the first k elements of the array
    #     for i in range(k):
    #         # 3. get the current element
    #         curr = arr[i]
    #
    #         # 4. check if the current element has at most two digits
    #         if digits(curr) <= 2:
    #             # 5. if so, add it to the sum
    #             sum += curr
    #
    #     # 6. return the sum
    #     return sum

    # 2. Use a counter
    #   - use a counter for the number of elements with at most two digits
    #     - for each element in the first k elements, check if it has at most two digits
    #     - if it does, increment the counter
    #   - return the sum
    #
    #   Time: O(k)
    #   Space: O(1)
    #
    # def add_elements(arr, k):
    #     # 1. initialize our sum to 0
    #     sum = 0
    #
    #     # 2. initialize our counter to 0
    #     counter = 0
    #
    #     # 3. loop through the first k elements of the array
    #     for i in range(k):
    #         # 4. get the current element
    #         curr = arr[i