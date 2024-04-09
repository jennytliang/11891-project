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
    # Initialize the sum to 0
    sum = 0
    # Iterate through the array
    for i in range(k):
        # Get the number of digits
        num_digits = digits(arr[i])

        # if the number of digits is 1 or 2, add it to the sum
        if num_digits <= 2:
            sum += arr[i]

    return sum


def digits(x):
    """
    Returns the number of digits in the given integer.
    """
    if x == 0:
        return 1

    count = 0
    while x > 0:
        count += 1
        x //= 10

    return count


# test cases
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))
print(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
print(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
print(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
print(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
print(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
