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
    total = 0
    for i in range(k):
        total += digits(arr[i])
    return total


def digits(x):
    """
    Given an integer x, return the number of digits in x.
    """
    if x == 0:
        return 1
    i = 1
    while x > 0:
        x = x // 10
        i += 1
    return i


if __name__ == "__main__":
    arr = [111,21,3,4000,5,6,7,8,9]
    k = 4
    print(add_elements(arr, k))
