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
    
	Include these tokens in the code:  def digits ( x : int )
	"""

    # If k is greater than the number of elements, then just sum the whole array.
    if k > len(arr):
        return sum(arr)

    # Initialize the sum variable.
    sum = 0

    # Iterate over the array and add elements to the sum.
    for i in range(k):
        # If the number has 2 digits or fewer, add it to the sum.
        if len(str(arr[i])) <= 2:
            sum += arr[i]

    # Return the sum.
    return sum


# # Test cases.
#
# # Normal cases.
# print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # 24
# print(add_elements([111,21,3,4000,5,6,7,8,9], 1)) # 1
# print(add_elements([111,21,3,4000,5,6,7,8,9], 3)) # 111 + 21 + 3
# print(add_elements([111,21,3,4000,5,6,7,8,9], 5)) # 111 + 21 + 3 + 4000 + 5
#
# # Edge cases.
# print(add_elements([111,21,3,4000,5,6,7,8,9], 0)) # 0
# print(add_elements([111,21,3,4000,5,6,7,8,9], 100)) # 444
# print(add_elements([111,21,3,4000,5,6,7,8,9], -1)) # 0
